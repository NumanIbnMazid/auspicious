from django.shortcuts import render
from django.views.generic import TemplateView
from .models import (
    Project, NewsCategory
)
# from .forms import (
#     ProjectManageForm,
# )

from .forms import *

from util.helpers import (
    validate_normal_form, simple_context_data, get_simple_object, delete_simple_object, user_has_permission
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
        context['list_objects'] = Project.objects.all().order_by('-id')
        context['list_template'] = None
        context['fields_count'] = len(Project._meta.get_fields()) + 1
        context['fields'] = dict([(f.name, f.verbose_name)
                                  for f in Project._meta.fields + Project._meta.many_to_many])
        context['fields_to_hide_in_table'] = ["slug"]
        context["update_url"] = "dashboard:update_project"
        context["delete_url"] = "dashboard:delete_project"
        context["detail_url"] = "dashboard:project_detail"
        context['namespace'] = 'project'
        context['can_add_change'] = True if self.request.user.has_perm(
            'dashboard.add_project') and self.request.user.has_perm('dashboard.change_project') else False
        context['can_view'] = self.request.user.has_perm(
            'dashboard.view_project')
        context['can_delete'] = self.request.user.has_perm(
            'dashboard.delete_project')
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
        context["create_url"] = "dashboard:create_project"
        context["update_url"] = "dashboard:update_project"
        context["delete_url"] = "dashboard:delete_project"
        context["list_url"] = "dashboard:create_project"
        context['can_add_change'] = True if self.request.user.has_perm(
            'dashboard.add_project') and self.request.user.has_perm('dashboard.change_project') else False
        context['can_view'] = self.request.user.has_perm(
            'dashboard.view_project')
        context['can_delete'] = self.request.user.has_perm(
            'dashboard.delete_project')
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
        context['list_objects'] = Project.objects.all().order_by('-id')
        context['list_template'] = None
        context['fields_count'] = len(Project._meta.get_fields()) + 1
        context['fields'] = dict([(f.name, f.verbose_name)
                                  for f in Project._meta.fields + Project._meta.many_to_many])
        context['fields_to_hide_in_table'] = ["slug"]
        context["update_url"] = "dashboard:update_project"
        context["delete_url"] = "dashboard:delete_project"
        context["detail_url"] = "dashboard:project_detail"
        context['namespace'] = 'project'
        context['can_add_change'] = True if self.request.user.has_perm(
            'dashboard.add_project') and self.request.user.has_perm('dashboard.change_project') else False
        context['can_view'] = self.request.user.has_perm(
            'dashboard.view_project')
        context['can_delete'] = self.request.user.has_perm(
            'dashboard.delete_project')
        return context


@csrf_exempt
def delete_project(request):
    return delete_simple_object(request=request, key='slug', model=Project, redirect_url="dashboard:create_project")





# # -------------------------------------------------------------------
# #                               News Category
# # -------------------------------------------------------------------

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
        context['list_objects'] = NewsCategory.objects.all().order_by('-id')
        context['list_template'] = None
        context['fields_count'] = len(NewsCategory._meta.get_fields()) + 1
        context['fields'] = dict([(f.name, f.verbose_name)
                                  for f in NewsCategory._meta.fields + NewsCategory._meta.many_to_many])
        context['fields_to_hide_in_table'] = ["slug"]
        context["update_url"] = "dashboard:update_news_category"
        context["delete_url"] = "dashboard:delete_news_category"
        context["detail_url"] = "dashboard:news_category_detail"
        context['namespace'] = 'news_category'
        context['can_add_change'] = True if self.request.user.has_perm(
            'dashboard.add_news_category') and self.request.user.has_perm('dashboard.change_news_category') else False
        context['can_view'] = self.request.user.has_perm(
            'dashboard.view_news_category')
        context['can_delete'] = self.request.user.has_perm(
            'dashboard.delete_news_category')
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
        context["create_url"] = "dashboard:create_news_category"
        context["update_url"] = "dashboard:update_news_category"
        context["delete_url"] = "dashboard:delete_news_category"
        context["list_url"] = "dashboard:create_news_category"
        context['can_add_change'] = True if self.request.user.has_perm(
            'dashboard.add_news_category') and self.request.user.has_perm('dashboard.change_news_category') else False
        context['can_view'] = self.request.user.has_perm(
            'dashboard.view_news_category')
        context['can_delete'] = self.request.user.has_perm(
            'dashboard.delete_news_category')
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
        context['list_objects'] = NewsCategory.objects.all().order_by('-id')
        context['list_template'] = None
        context['fields_count'] = len(NewsCategory._meta.get_fields()) + 1
        context['fields'] = dict([(f.name, f.verbose_name)
                                  for f in NewsCategory._meta.fields + NewsCategory._meta.many_to_many])
        context['fields_to_hide_in_table'] = ["id"]
        context["update_url"] = "dashboard:update_news_category"
        context["delete_url"] = "dashboard:delete_news_category"
        context["detail_url"] = "dashboard:news_category_detail"
        context['namespace'] = 'news_category'
        context['can_add_change'] = True if self.request.user.has_perm(
            'dashboard.add_news_category') and self.request.user.has_perm('dashboard.change_news_category') else False
        context['can_view'] = self.request.user.has_perm(
            'dashboard.view_news_category')
        context['can_delete'] = self.request.user.has_perm(
            'dashboard.delete_news_category')
        return context


@csrf_exempt
def delete_news_category(request):
    return delete_simple_object(request=request, key='id', model=NewsCategory, redirect_url="dashboard:create_news_category")
