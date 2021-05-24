from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
    Project, NewsCategory, News, Gallery
)
from .forms import (
    ProjectManageForm, NewsCategoryManageForm,NewsManageForm, GalleryManageForm
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


# # -------------------------------------------------------------------
# #                             Dashboard
# # -------------------------------------------------------------------
class DashboardView(TemplateView):
    template_name = 'dashboard/base.html'


# # -------------------------------------------------------------------
# #                               Project
# # -------------------------------------------------------------------

def get_project_common_contexts(request):
    common_contexts = get_simple_context_data(
        request=request, app_namespace="dashboard", model_namespace="project", model=Project, list_template=None, fields_to_hide_in_table=["slug"]
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
        request=request, app_namespace="dashboard", model_namespace="news_category", model=NewsCategory, list_template=None, fields_to_hide_in_table=[]
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
        request=request, app_namespace="dashboard", model_namespace="news", model=News, list_template=None, fields_to_hide_in_table=['slug']
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
        request=request, app_namespace="dashboard", model_namespace="gallery", model=Gallery, list_template=None, fields_to_hide_in_table=["slug"]
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

