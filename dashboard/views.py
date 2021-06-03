from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
    Project, NewsCategory, News, Gallery, Client, SocialAccount,
    JobPosition, Job, Contact, ProjectCategory
)
from .forms import (
    ProjectManageForm, NewsCategoryManageForm,NewsManageForm, GalleryManageForm, ClientManageForm, SocialAccountManageForm,
    JobPositionManageForm, JobManageForm, ContactManageForm, ProjectCategoryManageForm
)

from util.helpers import (
    validate_normal_form, get_simple_context_data, get_simple_object, delete_simple_object, user_has_permission
)
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
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView
from django.http import HttpResponse

# # -------------------------------------------------------------------
# #                             Dashboard
# # -------------------------------------------------------------------
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
def delete_project_category(request):
    return delete_simple_object(request=request, key='id', model=ProjectCategory, redirect_url="dashboard:create_project_category")





# # -------------------------------------------------------------------
# #                               Project
# # -------------------------------------------------------------------

def get_project_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="project", model=Project, list_template=None, fields_to_hide_in_table=["id","id","slug","updated_at"]
    )
    return common_contexts


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
def delete_project(request):
    return delete_simple_object(request=request, key='slug', model=Project, redirect_url="dashboard:create_project")





# # -------------------------------------------------------------------
# #                               News Category
# # -------------------------------------------------------------------


def get_news_category_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="news_category", model=NewsCategory, list_template=None, fields_to_hide_in_table=["id","updated_at"]
    )
    return common_contexts

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


class NewsCategoryDetailView(DetailView):
    template_name = "dashboard/snippets/detail-common.html"

    def get_object(self):
        return get_simple_object(key='id', model=NewsCategory, self=self)

    def get_context_data(self, **kwargs):
        context = super(
            NewsCategoryDetailView, self
        ).get_context_data(**kwargs)
        context['page_title'] = f'NewsCategory - {self.get_object().title} Detail'
        context['page_short_title'] = f'NewsCategory - {self.get_object().title} Detail'
        for key, value in get_news_category_common_contexts(request=self.request).items():
            context[key] = value
        return context


class NewsCategoryUpdateView(UpdateView):
    template_name = 'dashboard/snippets/manage.html'
    form_class = NewsCategoryManageForm

    def get_object(self):
        return get_simple_object(key="id", model=NewsCategory, self=self)

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
def delete_news_category(request):
    return delete_simple_object(request=request, key='id', model=NewsCategory, redirect_url="dashboard:create_news_category")


# # -------------------------------------------------------------------
# #                               News
# # -------------------------------------------------------------------


def get_news_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="news", model=News, list_template=None, fields_to_hide_in_table=["id",'slug',"updated_at"]
    )
    return common_contexts

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
def delete_contact(request):
    return delete_simple_object(request=request, key='id', model=Contact, redirect_url="dashboard:create_contact")
