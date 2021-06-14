from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
    Project, NewsCategory, News, Gallery, Client, SocialAccount,
    JobPosition, Job, Contact, ProjectCategory, Career
)
from .forms import (
    ProjectManageForm, NewsCategoryManageForm,NewsManageForm, GalleryManageForm, ClientManageForm, SocialAccountManageForm,
    JobPositionManageForm, JobManageForm, ContactManageForm, ProjectCategoryManageForm, JobApplicationManageForm, JobStatusManageForm, CVManageForm
)

from util.helpers import (
    validate_normal_form, get_simple_context_data, get_simple_object, delete_simple_object, user_has_permission
)
from util.decorators import (
    has_dashboard_permission_required
)
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import Context
from django.contrib import messages
from django import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, ListView
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives

dashboard_decorators = [login_required, has_dashboard_permission_required]

# # -------------------------------------------------------------------
# #                             Dashboard
# # -------------------------------------------------------------------


@method_decorator(dashboard_decorators, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'dashboard/base.html'




# # -------------------------------------------------------------------
# #                               Project Category
# # -------------------------------------------------------------------

def get_project_category_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="project_category", model=ProjectCategory, list_template=None, fields_to_hide_in_table=["id","updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class ProjectCategoryCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = ProjectCategoryManageForm

    def form_valid(self, form, **kwargs):
        title = form.instance.title
        field_qs = ProjectCategory.objects.filter(
            title__iexact=title
        )
        result = validate_normal_form(
            field='title', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard:create_project_category')

    def get_context_data(self, **kwargs):
        context = super(
            ProjectCategoryCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Project Category'
        context['page_short_title'] = 'Create Project Category'
        for key, value in get_project_category_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class ProjectCategoryDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='id', model=ProjectCategory, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            ProjectCategoryDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'ProjectCategory - {self.get_object().title} Detail'
        context['page_short_title'] = f'ProjectCategory - {self.get_object().title} Detail'
        for key, value in get_project_category_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class ProjectCategoryUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = ProjectCategoryManageForm

    def get_object(self):
        return get_simple_object(key="id", model=ProjectCategory, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_project_category')

    def form_valid(self, form):
        self.object = self.get_object()
        title = form.instance.title
        if not self.object.title == title:
            field_qs = ProjectCategory.objects.filter(
                title__iexact=title
            )
            result = validate_normal_form(
                field='title', field_qs=field_qs,
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
            ProjectCategoryUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update Project Category"{self.get_object().title}"'
        context['page_short_title'] = f'Update Project Category"{self.get_object().title}"'
        for key, value in get_project_category_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_project_category(request):
    return delete_simple_object(request=request, key='id', model=ProjectCategory, redirect_url="dashboard:create_project_category")





# # -------------------------------------------------------------------
# #                               Project
# # -------------------------------------------------------------------

def get_project_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="project", model=Project, list_template=None, fields_to_hide_in_table=["id","slug","updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class ProjectCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = ProjectManageForm

    def form_valid(self, form, **kwargs):
        name = form.instance.name
        field_qs = Project.objects.filter(
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
        return reverse('dashboard:create_project')

    def get_context_data(self, **kwargs):
        context = super(
            ProjectCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Project'
        context['page_short_title'] = 'Create Project'
        for key, value in get_project_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class ProjectDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='slug', model=Project, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            ProjectDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Project - {self.get_object().name} Detail'
        context['page_short_title'] = f'Project - {self.get_object().name} Detail'
        for key, value in get_project_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class ProjectUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = ProjectManageForm

    def get_object(self):
        return get_simple_object(key="slug", model=Project, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_project')

    def form_valid(self, form):
        self.object = self.get_object()
        name = form.instance.name
        if not self.object.name == name:
            field_qs = Project.objects.filter(
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
            ProjectUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update Project "{self.get_object().name}"'
        context['page_short_title'] = f'Update Project "{self.get_object().name}"'
        for key, value in get_project_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_project(request):
    return delete_simple_object(request=request, key='slug', model=Project, redirect_url="dashboard:create_project")





# # -------------------------------------------------------------------
# #                               News Category
# # -------------------------------------------------------------------


def get_news_category_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="news_category", model=NewsCategory, list_template=None, fields_to_hide_in_table=["id","updated_at","slug"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class NewsCategoryCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = NewsCategoryManageForm

    def form_valid(self, form, **kwargs):
        title = form.instance.title
        field_qs = NewsCategory.objects.filter(
            title__iexact=title
        )
        result = validate_normal_form(
            field='title', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard:create_news_category')

    def get_context_data(self, **kwargs):
        context = super(
            NewsCategoryCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create News Category'
        context['page_short_title'] = 'Create News Category'
        for key, value in get_news_category_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class NewsCategoryDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='slug', model=NewsCategory, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            NewsCategoryDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'NewsCategory - {self.get_object().title} Detail'
        context['page_short_title'] = f'NewsCategory - {self.get_object().title} Detail'
        for key, value in get_news_category_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class NewsCategoryUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = NewsCategoryManageForm

    def get_object(self):
        return get_simple_object(key="slug", model=NewsCategory, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_news_category')

    def form_valid(self, form):
        self.object = self.get_object()
        title = form.instance.title
        if not self.object.title == title:
            field_qs = NewsCategory.objects.filter(
                title__iexact=title
            )
            result = validate_normal_form(
                field='title', field_qs=field_qs,
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
            NewsCategoryUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update News Category "{self.get_object().title}"'
        context['page_short_title'] = f'Update News Category "{self.get_object().title}"'
        for key, value in get_news_category_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_news_category(request):
    return delete_simple_object(request=request, key='slug', model=NewsCategory, redirect_url="dashboard:create_news_category")


# # -------------------------------------------------------------------
# #                               News
# # -------------------------------------------------------------------


def get_news_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="news", model=News, list_template=None, fields_to_hide_in_table=["id",'slug',"updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class NewsCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = NewsManageForm

    def form_valid(self, form, **kwargs):
        title = form.instance.title
        field_qs = News.objects.filter(
            title__iexact=title
        )
        result = validate_normal_form(
            field='title', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard:create_news')

    def get_context_data(self, **kwargs):
        context = super(
            NewsCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create News'
        context['page_short_title'] = 'Create News'
        for key, value in get_news_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class NewsDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='slug', model=News, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            NewsDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'News- {self.get_object().title} Detail'
        context['page_short_title'] = f'News - {self.get_object().title} Detail'
        for key, value in get_news_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class NewsUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = NewsManageForm

    def get_object(self):
        return get_simple_object(key="slug", model=News, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_news')

    def form_valid(self, form):
        self.object = self.get_object()
        title = form.instance.title
        if not self.object.title == title:
            field_qs = News.objects.filter(
                title__iexact=title
            )
            result = validate_normal_form(
                field='title', field_qs=field_qs,
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
            NewsUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update News Category "{self.get_object().title}"'
        context['page_short_title'] = f'Update News Category "{self.get_object().title}"'
        for key, value in get_news_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_news(request):
    return delete_simple_object(request=request, key='slug', model=News, redirect_url="dashboard:create_news")



# # -------------------------------------------------------------------
# #                               Gallery
# # -------------------------------------------------------------------

def get_gallery_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="gallery", model=Gallery, list_template=None, fields_to_hide_in_table=["id","slug","updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class GalleryCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = GalleryManageForm

    def form_valid(self, form, **kwargs):
        title = form.instance.title
        field_qs = Gallery.objects.filter(
            title__iexact=title
        )
        result = validate_normal_form(
            field='gallery', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard:create_gallery')

    def get_context_data(self, **kwargs):
        context = super(
            GalleryCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Gallery'
        context['page_short_title'] = 'Create Gallery'
        for key, value in get_gallery_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class GalleryDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='slug', model=Gallery, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            GalleryDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Gallery - {self.get_object().title} Detail'
        context['page_short_title'] = f'Gallery - {self.get_object().title} Detail'
        for key, value in get_gallery_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class GalleryUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = GalleryManageForm

    def get_object(self):
        return get_simple_object(key="slug", model=Gallery, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_gallery')

    def form_valid(self, form):
        self.object = self.get_object()
        title = form.instance.title
        if not self.object.title == title:
            field_qs = Gallery.objects.filter(
                title__iexact=title
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
            GalleryUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update Gallery "{self.get_object().title}"'
        context['page_short_title'] = f'Update Gallery "{self.get_object().title}"'
        for key, value in get_gallery_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_gallery(request):
    return delete_simple_object(request=request, key='slug', model=Gallery, redirect_url="dashboard:create_gallery")



# # -------------------------------------------------------------------
# #                               Client
# # -------------------------------------------------------------------

def get_client_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="client", model=Client, list_template=None, fields_to_hide_in_table=["id","slug","updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class ClientCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = ClientManageForm

    def form_valid(self, form, **kwargs):
        name = form.instance.name
        field_qs = Client.objects.filter(
            name__iexact=name
        )
        result = validate_normal_form(
            field='client', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard:create_client')

    def get_context_data(self, **kwargs):
        context = super(
            ClientCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Client'
        context['page_short_title'] = 'Create Client'
        for key, value in get_client_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class ClientDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='slug', model=Client, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            ClientDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Client - {self.get_object().name} Detail'
        context['page_short_title'] = f'Client - {self.get_object().name} Detail'
        for key, value in get_client_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class ClientUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = ClientManageForm

    def get_object(self):
        return get_simple_object(key="slug", model=Client, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_client')

    def form_valid(self, form):
        self.object = self.get_object()
        name = form.instance.name
        if not self.object.name == name:
            field_qs = Client.objects.filter(
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
            ClientUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update Client "{self.get_object().name}"'
        context['page_short_title'] = f'Update Gallery "{self.get_object().name}"'
        for key, value in get_client_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_client(request):
    return delete_simple_object(request=request, key='slug', model=Client, redirect_url="dashboard:create_client")




# # -------------------------------------------------------------------
# #                               Social Account
# # -------------------------------------------------------------------

def get_social_account_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="social_account", model=SocialAccount, list_template=None, fields_to_hide_in_table=["id","updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class SocialAccountCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = SocialAccountManageForm

    def form_valid(self, form, **kwargs):
        title = form.instance.title
        field_qs = SocialAccount.objects.filter(
            title__iexact=title
        )
        result = validate_normal_form(
            field='social_account', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard:create_social_account')

    def get_context_data(self, **kwargs):
        context = super(
            SocialAccountCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Social Account'
        context['page_short_title'] = 'Create Social Account'
        for key, value in get_social_account_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class SocialAccountDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='id', model=SocialAccount, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            SocialAccountDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'SocialAccount - {self.get_object().title} Detail'
        context['page_short_title'] = f'SocialAccount - {self.get_object().title} Detail'
        for key, value in get_social_account_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class SocialAccountUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = SocialAccountManageForm

    def get_object(self):
        return get_simple_object(key="id", model=SocialAccount, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_social_account')

    def form_valid(self, form):
        self.object = self.get_object()
        title = form.instance.title
        if not self.object.title == title:
            field_qs = SocialAccount.objects.filter(
                title__iexact=title
            )
            result = validate_normal_form(
                field='title', field_qs=field_qs,
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
            SocialAccountUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update Social Account "{self.get_object().title}"'
        context['page_short_title'] = f'Update Social Account "{self.get_object().title}"'
        for key, value in get_social_account_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_social_account(request):
    return delete_simple_object(request=request, key='id', model=SocialAccount, redirect_url="dashboard:create_social_account")




# # -------------------------------------------------------------------
# #                               Job Position
# # -------------------------------------------------------------------

def get_job_position_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="job_position", model=JobPosition, list_template=None, fields_to_hide_in_table=["id","updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class JobPositionCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = JobPositionManageForm

    def form_valid(self, form, **kwargs):
        title = form.instance.title
        field_qs = JobPosition.objects.filter(
            title__iexact=title
        )
        result = validate_normal_form(
            field='job_position', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard:create_job_position')

    def get_context_data(self, **kwargs):
        context = super(
            JobPositionCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Job Position'
        context['page_short_title'] = 'Create Job Position'
        for key, value in get_job_position_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class JobPositionDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='id', model=JobPosition, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            JobPositionDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'JobPosition - {self.get_object().title} Detail'
        context['page_short_title'] = f'JobPosition - {self.get_object().title} Detail'
        for key, value in get_job_position_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class JobPositionUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = JobPositionManageForm

    def get_object(self):
        return get_simple_object(key="id", model=JobPosition, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_job_position')

    def form_valid(self, form):
        self.object = self.get_object()
        title = form.instance.title
        if not self.object.title == title:
            field_qs = JobPosition.objects.filter(
                title__iexact=title
            )
            result = validate_normal_form(
                field='title', field_qs=field_qs,
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
            JobPositionUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update Job Position "{self.get_object().title}"'
        context['page_short_title'] = f'Update Job Position "{self.get_object().title}"'
        for key, value in get_job_position_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_job_position(request):
    return delete_simple_object(request=request, key='id', model=JobPosition, redirect_url="dashboard:create_job_position")



# # -------------------------------------------------------------------
# #                               Job
# # -------------------------------------------------------------------

def get_job_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="job", model=Job, list_template=None, fields_to_hide_in_table=["id","slug", 'updated_at','id']
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class JobCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = JobManageForm

    def form_valid(self, form, **kwargs):
        messages.add_message(
            self.request, messages.SUCCESS,
            "Job Created Successfully"
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dashboard:create_job')

    def get_context_data(self, **kwargs):
        context = super(
            JobCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Job'
        context['page_short_title'] = 'Create Job'
        for key, value in get_job_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class JobDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='slug', model=Job, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            JobDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Job - {self.get_object().job_position.title} Detail'
        context['page_short_title'] = f'Job - {self.get_object().job_position.title} Detail'
        for key, value in get_job_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class JobUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = JobManageForm

    def get_object(self):
        return get_simple_object(key="slug", model=Job, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_job')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, "Job Updated Successfully!"
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(
            JobUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update Job "{self.get_object().job_position.title}"'
        context['page_short_title'] = f'Update Job "{self.get_object().job_position.title}"'
        for key, value in get_job_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_job(request):
    return delete_simple_object(request=request, key='slug', model=Job, redirect_url="dashboard:create_job")




# # -------------------------------------------------------------------
# #                               Contact
# # -------------------------------------------------------------------

def get_contact_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="contact", model=Contact, list_template=None, fields_to_hide_in_table=["id","updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class ContactCreateView(CreateView):
    template_name = "dashboard/snippets/manage.html"
    form_class = ContactManageForm

    def form_valid(self, form, **kwargs):
        phone1 = form.instance.phone1
        field_qs = Contact.objects.filter(
            phone1__iexact=phone1
        )
        result = validate_normal_form(
            field='contact', field_qs=field_qs,
            form=form, request=self.request
        )
        if result == 1:
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashboard:create_contact')

    def get_context_data(self, **kwargs):
        context = super(
            ContactCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Contact'
        context['page_short_title'] = 'Create Contact'
        for key, value in get_contact_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class ContactDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='id', model=Contact, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            ContactDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Contact - {self.get_object().phone1} Detail'
        context['page_short_title'] = f'Contact - {self.get_object().phone1} Detail'
        for key, value in get_contact_common_contexts(request=self.request).items():
            context[key] = value
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class ContactUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = ContactManageForm

    def get_object(self):
        return get_simple_object(key="id", model=Contact, self=self)

    def get_success_url(self):
        return reverse('dashboard:create_contact')

    def form_valid(self, form):
        self.object = self.get_object()
        phone1 = form.instance.phone1
        if not self.object.phone1 == phone1:
            field_qs = Contact.objects.filter(
                phone1__iexact=phone1
            )
            result = validate_normal_form(
                field='phone1', field_qs=field_qs,
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
            ContactUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'Update Contact"{self.get_object().phone1}"'
        context['page_short_title'] = f'Update Contact "{self.get_object().phone1}"'
        for key, value in get_contact_common_contexts(request=self.request).items():
            context[key] = value
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_contact(request):
    return delete_simple_object(request=request, key='id', model=Contact, redirect_url="dashboard:create_contact")


# # -------------------------------------------------------------------
# #                              Career
# # -------------------------------------------------------------------

### Job Application ###

def get_job_application_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="career", model=Career, list_template=None, fields_to_hide_in_table=["id", "slug", "updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class JobApplicationListView(ListView):
    template_name = "dashboard/pages/job-application/list.html"

    def get_queryset(self):
        qs = Career.objects.filter(
            ~Q(job__id=None)
        )
        if qs.exists():
            return qs
        return None

    def get_context_data(self, **kwargs):
        context = super(JobApplicationListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Job Application List'
        context['page_short_title'] = 'Job Application List'
        for key, value in get_job_application_common_contexts(request=self.request).items():
            context[key] = value
        context['list_objects'] = self.get_queryset()
        context['list_template'] = "dashboard/pages/job-application/datatable.html"
        context['detail_url'] = "dashboard:job_application_detail"
        context['update_url'] = "dashboard:job_application_update"
        context['delete_url'] = "dashboard:delete_job_application"
        context['create_url'] = None
        context['list_url'] = "dashboard:job_application_list"
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class JobApplicationUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = JobApplicationManageForm

    def get_object(self):
        return get_simple_object(key="slug", model=Career, self=self)

    def get_success_url(self):
        return reverse('dashboard:job_application_list')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, "Updated Successfully!"
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(
            JobApplicationUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Update Application'
        context['page_short_title'] = 'Update Application'
        for key, value in get_job_application_common_contexts(request=self.request).items():
            context[key] = value
        context['update_url'] = "dashboard:job_application_update"
        context['detail_url'] = "dashboard:job_application_detail"
        context['delete_url'] = "dashboard:delete_job_application"
        context['create_url'] = None
        context['list_template'] = "dashboard/pages/job-application/datatable.html"
        context['list_objects'] = Career.objects.filter(
            ~Q(job__id=None)
        )
        context['list_url'] = "dashboard:job_application_list"
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class JobApplicationDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='slug', model=Career, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            JobApplicationDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Job Application Detail'
        context['page_short_title'] = 'Job Application Detail'
        for key, value in get_job_application_common_contexts(request=self.request).items():
            context[key] = value
        context['delete_url'] = "dashboard:delete_job_application"
        context['create_url'] = None
        context['update_url'] = "dashboard:job_application_update"
        context['detail_url'] = "dashboard:job_application_detail"
        context['list_template'] = "dashboard/pages/job-application/datatable.html"
        context['list_objects'] = Career.objects.filter(
            ~Q(job__id=None)
        )
        context['list_url'] = "dashboard:job_application_list"
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_job_application(request):
    return delete_simple_object(request=request, key='slug', model=Career, redirect_url="dashboard:job_application_list")


### CV ###

def get_cv_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="career", model=Career, list_template=None, fields_to_hide_in_table=["id", "slug", "updated_at"]
    )
    return common_contexts


@method_decorator(dashboard_decorators, name='dispatch')
class CVListView(ListView):
    template_name = "dashboard/pages/job-application/list.html"

    def get_queryset(self):
        qs = Career.objects.filter(
            Q(job__id=None)
        )
        if qs.exists():
            return qs
        return None

    def get_context_data(self, **kwargs):
        context = super(CVListView, self).get_context_data(**kwargs)
        context['page_title'] = 'CV List'
        context['page_short_title'] = 'CV List'
        for key, value in get_cv_common_contexts(request=self.request).items():
            context[key] = value
        context['list_objects'] = self.get_queryset()
        context['list_template'] = "dashboard/pages/job-application/datatable.html"
        context['detail_url'] = "dashboard:cv_detail"
        context['update_url'] = "dashboard:cv_update"
        context['delete_url'] = "dashboard:delete_cv"
        context['create_url'] = None
        context['list_url'] = "dashboard:cv_list"
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class CVUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = CVManageForm

    def get_object(self):
        return get_simple_object(key="slug", model=Career, self=self)

    def get_success_url(self):
        return reverse('dashboard:cv_list')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, "Updated Successfully!"
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(
            CVUpdateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Update CV'
        context['page_short_title'] = 'Update CV'
        for key, value in get_cv_common_contexts(request=self.request).items():
            context[key] = value
        context['update_url'] = "dashboard:cv_update"
        context['detail_url'] = "dashboard:cv_detail"
        context['delete_url'] = "dashboard:delete_cv"
        context['create_url'] = None
        context['list_url'] = "dashboard:cv_list"
        context['list_template'] = "dashboard/pages/job-application/datatable.html"
        context['list_objects'] = Career.objects.filter(
            Q(job__id=None)
        )
        return context


@method_decorator(dashboard_decorators, name='dispatch')
class CVDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='slug', model=Career, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            CVDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'CV Detail'
        context['page_short_title'] = 'CV Detail'
        for key, value in get_cv_common_contexts(request=self.request).items():
            context[key] = value
        context['delete_url'] = "dashboard:delete_cv"
        context['create_url'] = None
        context['update_url'] = "dashboard:cv_update"
        context['detail_url'] = "dashboard:cv_detail"
        context['list_template'] = "dashboard/pages/job-application/datatable.html"
        context['list_objects'] = Career.objects.filter(
            Q(job__id=None)
        )
        context['list_url'] = "dashboard:cv_list"
        return context


@csrf_exempt
@has_dashboard_permission_required
@login_required
def delete_cv(request):
    return delete_simple_object(request=request, key='slug', model=Career, redirect_url="dashboard:cv_list")


# @csrf_exempt
@has_dashboard_permission_required
@login_required
def update_job_application_status(request, slug):
    url = reverse('home')
    career_qs = Career.objects.filter(
        slug=slug
    )

    if career_qs:

        career = career_qs.last()

        if not career.job == None:
            url = reverse("dashboard:job_application_list")
            page_title = "Update Application Status"
        else:
            url = reverse("dashboard:cv_list")
            page_title = "Update CV Status"

        if request.method == "POST":
            form = JobStatusManageForm(
                request.POST, career_object=career_qs.last()
            )

            status = request.POST.get('status')

            finalized_status = "Under Review" if status == "Review" else status

            if not career.job == None:
                mail_subject = f"Your application status for the position '{career.job.job_position.title}' is : {finalized_status}"
            else:
                mail_subject = f"Your CV is : {finalized_status}"
            mail_body = request.POST.get('mail_body')

            # Save Status in DB
            career.status = status
            career.save()

            message = mail_body
            mail_from = settings.MAIL_FROM
            mail_to = career.user.email
            mail_text = 'Please do not Reply'
            html_content = "Hi " + career.user.user_profile.get_fullname() + "!<br><br>" + f"<h3>{mail_subject}</h3>" + "<br>" + message + \
                "<br>Have a nice day."
            msg = EmailMultiAlternatives(
                mail_subject, mail_text, mail_from, [mail_to]
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            messages.add_message(request, messages.SUCCESS,
                                 "Updated Successfully!"
                                 )
            return HttpResponseRedirect(url)

        else:
            form = JobStatusManageForm(career_object=career_qs.last())

        context = {
            "form": form,
            "can_change": request.user.has_perm(
                'dashboard.change_career'
            ),
            "page_title": page_title,
            "page_short_title": page_title,
        }

    else:
        messages.add_message(request, messages.ERROR,
                             "Job Application Not Found!"
                             )
        return HttpResponseRedirect(url)
    return render(request, "dashboard/pages/job-application/update-status.html", context)
