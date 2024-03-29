from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, ListView
from django.template import Context
from django.contrib import messages
from django import forms
from util.helpers import (
    validate_normal_form, get_simple_context_data, get_simple_object, delete_simple_object, user_has_permission
)
from .models import Profile
from django.conf import settings
from .forms import UserCreateForm, UserUpdateForm, ProfileForm
from django.contrib.auth.models import User, Group, Permission
from .forms import UserGroupForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count, Min, Q, query_utils

# # -------------------------------------------------------------------
# #                           Group
# # -------------------------------------------------------------------

class GroupCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = UserGroupForm

    def form_valid(self, form, **kwargs):
        name = form.instance.name
        field_qs = Group.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='name', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('create_group')

    def get_context_data(self, **kwargs):
        context = super(
            GroupCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Group'
        context['page_short_title'] = 'Create Group'
        context['list_objects'] = Group.objects.all().order_by('-id')
        context['list_template'] = None
        context['fields_count'] = len(Group._meta.get_fields()) + 1
        context['fields'] = dict([(f.name, f.verbose_name)
                                  for f in Group._meta.fields + Group._meta.many_to_many])
        context["update_url"] = "update_group"
        context["delete_url"] = "delete_group"
        context["detail_url"] = "group_detail"
        context['namespace'] = 'group'
        context['can_add_change'] = True if self.request.user.has_perm(
            'auth.add_group') or self.request.user.has_perm('auth.change_group') else False
        context['can_add'] = True if self.request.user.has_perm('auth.add_group') else False
        context['can_change'] = True if self.request.user.has_perm('auth.change_group') else False
        context['can_view'] = self.request.user.has_perm('auth.view_group')
        context['can_delete'] = self.request.user.has_perm('auth.delete_group')
        return context


class GroupDetailView(DetailView):
    template_name = "accounts/group-detail.html"

    def get_object(self):
        return get_simple_object(key='id', model=Group, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            GroupDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Group - {self.get_object().name} Detail'
        context['page_short_title'] = f'Group - {self.get_object().name} Detail'
        context["create_url"] = "create_group"
        context["update_url"] = "update_group"
        context["delete_url"] = "delete_group"
        context["list_url"] = "create_group"
        context['can_add_change'] = True if self.request.user.has_perm(
            'auth.add_group') == True or self.request.user.has_perm('auth.change_group') == True else False
        context['can_add'] = True if self.request.user.has_perm('auth.add_group') else False
        context['can_change'] = True if self.request.user.has_perm('auth.change_group') else False
        context['can_view'] = self.request.user.has_perm(
            'auth.view_group')
        context['can_delete'] = self.request.user.has_perm(
            'auth.delete_group')
        return context


class GroupUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = UserGroupForm

    def get_object(self):
        return get_simple_object(key="id", model=Group, self=self)

    def get_success_url(self):
        return reverse('create_group')

    def form_valid(self, form):
        self.object = self.get_object()
        name = form.instance.name
        if not self.object.name == name:
            field_qs = Group.objects.filter(
                name__iexact=name
            )
            result = validate_normal_form(
                field='name', field_qs=field_qs,
                form=form, request=self.request
            )
            if result == 1:
                return super().form_valid(form)
            else:
                return super().form_invalid(form)

        messages.add_message(
            self.request, messages.SUCCESS, "Updated Successfully!"
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(
            GroupUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Update Group'
        context['page_short_title'] = 'Update Group'
        context['list_objects'] = Group.objects.all().order_by('-id')
        context['list_template'] = None
        context['fields_count'] = len(Group._meta.get_fields()) + 1
        context['fields'] = dict([(f.name, f.verbose_name)
                                  for f in Group._meta.fields + Group._meta.many_to_many])
        context["update_url"] = "update_group"
        context["delete_url"] = "delete_group"
        context["detail_url"] = "group_detail"
        context['namespace'] = 'group'
        context['can_add_change'] = True if self.request.user.has_perm(
            'auth.add_group') == True or self.request.user.has_perm('auth.change_group') == True else False
        context['can_add'] = True if self.request.user.has_perm('auth.add_group') else False
        context['can_change'] = True if self.request.user.has_perm('auth.change_group') else False
        context['can_view'] = self.request.user.has_perm(
            'auth.view_group')
        context['can_delete'] = self.request.user.has_perm(
            'auth.delete_group')
        return context


@csrf_exempt
def delete_group(request):
    return delete_simple_object(request=request, key='id', model=Group, redirect_url="create_group")


# # -------------------------------------------------------------------
# #                           User
# # -------------------------------------------------------------------


def create_user(request):
    # Check Required Permission
    # if request.user.has_perm("auth.add_user") == False:
    #     return render(request, 'exceptions/access-denied.html')

    # context = Context()
    form = UserCreateForm()
    context = {
        'page_title': "Create Admin User",
        'page_short_title': "Create Admin User",
        'list_objects': User.objects.filter(
            Q(is_superuser = True) | ~Q(user_profile__created_by=None)
        ).order_by('-date_joined'),
        # 'list_objects': Profile.objects.filter(Q(user)),
        'list_template': "accounts/user-list.html",
        'fields_count': len(User._meta.get_fields()) + 1,
        'fields': dict([(f.name, f.verbose_name)
                        for f in User._meta.fields + User._meta.many_to_many]),
        'update_url': "update_user",
        'delete_url': "delete_user",
        'detail_url': "user_detail",
        'namespace': "admin-user",
        'object': User.objects.filter(username=request.user.username).first().user_profile,
        'form': form,
        'can_add_change': True if request.user.has_perm('auth.add_user') or request.user.has_perm('auth.change_user') else False,
        'can_add': True if request.user.has_perm('auth.add_user') else False,
        'can_change': True if request.user.has_perm('auth.change_user') else False,
        'can_view': request.user.has_perm('auth.view_user'),
        'can_delete': request.user.has_perm('auth.delete_user'),
        'is_admin_list': True
    }

    if request.method == "POST":
        form = UserCreateForm(request.POST)
        context["form"] = form

        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        gender = request.POST["gender"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirm_password"]
        if form.is_valid():
            user_groups = form.cleaned_data.get("user_groups")
            permissions = form.cleaned_data.get("permissions")
            try:
                user_obj = User(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    # gender=gender
                )
                user_obj.set_password(password)
                user_obj.save()

                # add user to group
                for user_group in user_groups:
                    group_qs = Group.objects.filter(name=user_group)
                    if group_qs.exists():
                        selected_group = group_qs.first()
                        selected_group.user_set.add(user_obj)
                    else:
                        messages.error(
                            request, 'Failed to add user to group!'
                        )

                # assign user permissions
                for permission in permissions:
                    permission_qs = Permission.objects.filter(name=permission.name)
                    if permission_qs.exists():
                        selected_permission = permission_qs.first()
                        user_obj.user_permissions.add(selected_permission)
                    else:
                        messages.error(
                            request, 'Failed to assign permission!'
                        )

                messages.success(
                    request, f'User {username} created successfully !'
                )
                context["form"] = UserCreateForm()
                return redirect("create_user")

            except Exception as E:
                messages.error(
                    request, 'Failed to create user!'
                )
    else:
        form = UserCreateForm()
    return render(request, 'dashboard/snippets/manage.html', context)


class UserDetailView(DetailView):
    template_name = "accounts/user-detail.html"

    def get_object(self):
        return get_simple_object(key='slug', model=Profile, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            UserDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'User - {self.get_object().get_dynamic_name()} Detail'
        context['page_short_title'] = f'User - {self.get_object().get_dynamic_name()} Detail'
        context["create_url"] = "create_user"
        context["update_url"] = "update_user"
        context["delete_url"] = "delete_user"
        context['can_add_change'] = True if self.request.user.has_perm(
            'auth.add_user') or self.request.user.has_perm('auth.change_user') else False
        context['can_add'] = True if self.request.user.has_perm('auth.add_user') else False
        context['can_change'] = True if self.request.user.has_perm('auth.change_user') else False
        context['can_view'] = self.request.user.has_perm('auth.view_user')
        context['can_delete'] = self.request.user.has_perm('auth.delete_user')
        return context


class ProfileUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = ProfileForm

    def get_object(self):
        qs = Profile.objects.filter(slug=self.kwargs['slug'])
        if qs.exists():
            return qs.first()
        return None

    def dispatch(self, request, *args, **kwargs):
        qs = Profile.objects.filter(slug=self.kwargs['slug'])
        obj = None
        if qs.exists():
            obj = qs.last()
            if not self.request.user.has_perm("auth.change_user"):
                messages.add_message(
                    self.request, messages.ERROR, "Not enough permission!"
                )
                return HttpResponseRedirect(reverse('home'))
            if obj.user.is_superuser == False and obj.created_by == None:
                messages.add_message(
                    self.request, messages.ERROR, "Update unavailable!"
                )
                return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(
                self.request, messages.ERROR, "Profile object not found!"
            )
            return HttpResponseRedirect(reverse('home'))
        return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = self.get_object()
        user_groups = form.cleaned_data.get("user_group")
        permissions = form.cleaned_data.get("permissions")
        # clear user groups
        self.object.user.groups.clear()
        # add user to group
        for user_group in user_groups:
            group_qs = Group.objects.filter(name=user_group)
            if group_qs.exists():
                selected_group = group_qs.first()
                # add new groups
                selected_group.user_set.add(self.object.user)
            else:
                messages.error(
                    self.request, 'Failed to add user to group!'
                )
        
        # clear user permissions
        self.object.user.user_permissions.clear()
        # assign user permissions
        for permission in permissions:
            permission_qs = Permission.objects.filter(name=permission.name)
            if permission_qs.exists():
                selected_permission = permission_qs.first()
                self.object.user.user_permissions.add(selected_permission)
            else:
                messages.error(
                    self.request, 'Failed to assign permission!'
                )

        username = self.request.POST.get("username")
        if not self.object.user.username == username:
            username_qs = User.objects.filter(
                username__iexact=username
            )
            if username_qs.exists():
                form.add_error(
                    'username', forms.ValidationError(
                        "This username is already exists! Please try another one."
                    )
                )
                return super().form_invalid(form)

        messages.add_message(
            self.request, messages.SUCCESS, "User has been updated successfully !"
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Update User'
        context['page_short_title'] = 'Update User'
        context['list_template'] = "accounts/user-list.html"
        context['list_objects'] = User.objects.all().order_by('-date_joined')
        context['fields_count'] = len(User._meta.get_fields()) + 1
        context['fields'] = dict([(f.name, f.verbose_name)
                                  for f in User._meta.fields + User._meta.many_to_many])
        context["update_url"] = "update_user"
        context["delete_url"] = "delete_user"
        context["detail_url"] = "user_detail"
        context['namespace'] = 'user'
        context['can_add_change'] = True if self.request.user.has_perm(
            'auth.add_user') or self.request.user.has_perm('auth.change_user') else False
        context['can_add'] = True if self.request.user.has_perm('auth.add_user') else False
        context['can_change'] = True if self.request.user.has_perm('auth.change_user') else False
        context['can_view'] = self.request.user.has_perm('auth.view_user')
        context['can_delete'] = self.request.user.has_perm('auth.delete_user')
        return context

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse('update_user', kwargs={'slug': slug})


@csrf_exempt
def delete_user(request):
    url = reverse('home')
    # user = request.user
    if request.method == "POST":
        slug = request.POST.get("id")
        profile_qs = Profile.objects.filter(slug=slug)
        if profile_qs.exists():
            user_qs = User.objects.filter(
                username=profile_qs.first().user.username)
            if user_qs.exists():
                user_qs.delete()
                messages.add_message(request, messages.SUCCESS,
                                     "User Deleted successfully!")
                url = reverse('create_user')
        else:
            messages.add_message(request, messages.WARNING,
                                 "Not found!")
    return HttpResponseRedirect(url)


### End User ###

def user_list(request):
    # Check Required Permission
    # if request.user.has_perm("auth.add_user") == False:
    #     return render(request, 'exceptions/access-denied.html')

    # context = Context()
    # form = UserCreateForm()
    context = {
        'page_title': "User List",
        'page_short_title': "User List",
        'list_objects': User.objects.filter
            (is_superuser = False, user_profile__created_by=None
        ).order_by('-date_joined'),
        # 'list_objects': Profile.objects.filter(Q(user)),
        'list_template': "accounts/user-list.html",
        'fields_count': len(User._meta.get_fields()) + 1,
        'fields': dict([(f.name, f.verbose_name)
                        for f in User._meta.fields + User._meta.many_to_many]),
        'update_url': None,
        'delete_url': "delete_user_list",
        'detail_url': "user_details",
        'namespace': "user",
        'object': User.objects.filter(username=request.user.username).first().user_profile,
        # 'form': form,
        'can_add_change': False if request.user.has_perm('auth.add_user') or request.user.has_perm('auth.change_user') else False,
        # 'can_add': True if request.user.has_perm('auth.add_user') else False,
        'can_change': True if request.user.has_perm('auth.change_user') else False,
        'can_view': True if request.user.has_perm('auth.view_user') else False,

    }
    return render(request, 'dashboard/snippets/manage.html', context)

class EndUserDetailView(DetailView):
    template_name = "accounts/user-detail.html"

    def get_object(self):
        return get_simple_object(key='slug', model=Profile, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            EndUserDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'User - {self.get_object().get_dynamic_name()} Detail'
        context['page_short_title'] = f'User - {self.get_object().get_dynamic_name()} Detail'
        context["create_url"] = None
        context["update_url"] = None
        context["delete_url"] = None
        context['can_add_change'] = True if self.request.user.has_perm(
            'auth.add_user') or self.request.user.has_perm('auth.change_user') else False
        context['can_add'] = True if self.request.user.has_perm('auth.add_user') else False
        context['can_change'] = True if self.request.user.has_perm('auth.change_user') else False
        context['can_view'] = self.request.user.has_perm('auth.view_user')
        context['can_delete'] = self.request.user.has_perm('auth.delete_user')
        return context
