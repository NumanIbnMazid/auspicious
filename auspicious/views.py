from django.views.generic import TemplateView, CreateView
from dashboard.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.urls import reverse
from .forms import CareerManageForm
from django.contrib import messages
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# class HomeView(request):
#     project_category_qs = ProjectCategory.objects.all()
#     project_qs = Project.objects.all()
#     contex = {'project_category_qs':project_category_qs,
#               'project_qs':project_qs}
#
#     # template_name = "index.html"
#     return render(request, 'index.html', contex)
#

# # -------------------------------------------------------------------
# #                              Home
# # -------------------------------------------------------------------


def home(request):
    today = timezone.datetime.now()
    datetime_today = datetime.strptime(
        str(today.date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
    project_category_qs = ProjectCategory.objects.all()
    project_lists = Project.objects.all()
    ongoing_project_lists = Project.objects.filter(developement_start_year__lte = datetime_today.year,developement_end_year = None)
    completed_project_lists = Project.objects.filter(developement_start_year__lte = datetime_today.year,developement_end_year__lte = datetime_today.year)
    latest_project_lists = Project.objects.filter(developement_end_year__lte = datetime_today.year, created_at__lte = today.date())[:4]
    latest_news_category_lists = NewsCategory.objects.all()
    latest_news_lists = News.objects.all()
    image_lists = Gallery.objects.all().order_by('?')
    clients_lists =  Client.objects.all().order_by('?')[:10]
    contact_qs = Contact.objects.all().last()
    context = {'project_category_qs':project_category_qs,
              'project_lists':project_lists,'ongoing_project_lists':ongoing_project_lists,
               'completed_project_lists':completed_project_lists,'latest_project_lists':latest_project_lists,
               'latest_news_category_lists':latest_news_category_lists,'latest_news_lists':latest_news_lists,
               'image_lists':image_lists,'contact_qs':contact_qs,'clients_lists':clients_lists}

    return render(request, 'index.html', context)
#

# # -------------------------------------------------------------------
# #                               About
# # -------------------------------------------------------------------

class AboutView(TemplateView):
    template_name = 'page/about.html'

# class CivilProjectView(TemplateView):
#     template_name = 'page/civil-project.html'

# # -------------------------------------------------------------------
# #                               Civil  Project
# # -------------------------------------------------------------------

def civilproject(request):
    today = timezone.datetime.now()
    datetime_today = datetime.strptime(
        str(today.date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
    ongoing_project_lists = Project.objects.filter(developement_end_year=None, category__title__icontains = 'Civil' ).order_by('id')
    completed_project_lists = Project.objects.filter(developement_end_year__lte = datetime_today.year, category__title__icontains = 'Civil' ).order_by('id')
    context ={'ongoing_project_lists':ongoing_project_lists,'completed_project_lists':completed_project_lists}
    return render(request, 'page/civil-project.html', context)

# class TelecomProjectView(TemplateView):
#     template_name = 'page/telecom-project.html'

# # -------------------------------------------------------------------
# #                               Telecom Project
# # -------------------------------------------------------------------


def telecomproject(request):
    today = timezone.datetime.now()
    datetime_today = datetime.strptime(
        str(today.date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
    ongoing_project_lists = Project.objects.filter(developement_end_year=None, category__title__icontains = 'Telecom' ).order_by('id')
    completed_project_lists = Project.objects.filter(developement_end_year__lte = datetime_today.year, category__title__icontains = 'Telecom' ).order_by('id')
    context ={'ongoing_project_lists':ongoing_project_lists,'completed_project_lists':completed_project_lists}
    return render(request, 'page/telecom-project.html', context)

# # -------------------------------------------------------------------
# #                              Civil Services
# # -------------------------------------------------------------------

class CivilServicesView(TemplateView):
    template_name = 'page/civil-service.html'

# # -------------------------------------------------------------------
# #                               Telecom Services
# # -------------------------------------------------------------------

class TelecomServicesView(TemplateView):
    template_name = 'page/telecom-service.html'

# class CareerView(TemplateView):
#     template_name = 'page/career.html'

# # -------------------------------------------------------------------
# #                               Career
# # -------------------------------------------------------------------

def career(request):
    last_job_qs = Job.objects.all().last()
    job_position_qs = JobPosition.objects.all()
    # job_count = Job.objects.filter(job_position =job_position_qs).count()
    # print(job_count)
    job_lists = Job.objects.filter(is_active = 'True').order_by("id")[1:5]
    context = {'last_job_qs':last_job_qs,'job_lists': job_lists,
               'job_position_qs':job_position_qs}
    return render(request, "page/career.html", context)

# # -------------------------------------------------------------------
# #                              Client  Details
# # -------------------------------------------------------------------

class ClientView(TemplateView):
    template_name = 'page/client.html'

# # -------------------------------------------------------------------
# #                              News
# # -------------------------------------------------------------------

# class NewsView(TemplateView):
#     template_name = 'page/news.html'

def news(request):
    news_lists= News.objects.all().order_by('-id')
    context ={'news_lists':news_lists}
    return render(request,'page/news.html', context )

# # -------------------------------------------------------------------
# #                               Contact
# # -------------------------------------------------------------------

# class ContactView(TemplateView):
#     template_name = 'page/contact.html'

def contact(request):
    contact_qs = Contact.objects.all().last()
    context ={'contact_qs':contact_qs}
    return render(request, 'page/contact.html', context)

# # -------------------------------------------------------------------
# #                               News Details
# # -------------------------------------------------------------------

class NewsDetailsView(TemplateView):
    template_name = 'page/news-details.html'

# # -------------------------------------------------------------------
# #                               Job Details
# # -------------------------------------------------------------------

def job_details(request, slug):
    job_qs = Job.objects.filter(slug = slug, is_active = 'True').first()
    job_position_qs = JobPosition.objects.all()
    contact_qs =  Contact.objects.all().last()
    context ={'job_qs':job_qs, 'job_position_qs':job_position_qs,
              'contact_qs':contact_qs}
    return render(request, "page/job-page.html", context)

# # -------------------------------------------------------------------
# #                              All Job Lists
# # -------------------------------------------------------------------

def all_job_lists(request):
    last_job_qs = Job.objects.all().last()
    job_lists = Job.objects.filter(is_active = 'True').order_by("id")
    context = {'last_job_qs':last_job_qs,'job_lists': job_lists}
    return render(request, "page/all-jobs.html", context)

# # -------------------------------------------------------------------
# #                              Filtered Job
# # -------------------------------------------------------------------

def filtered_job_lists(request, slug):
    job_qs = Job.objects.filter(
        job_position__slug__iexact=slug
    )
    context = {
        'job_lists':job_qs,
        'filtered_job_title': job_qs.first().job_position.title if len(job_qs) > 0 else ""
    }
    return render(request, "page/all-jobs.html", context)


# # -------------------------------------------------------------------
# #                               Job Apply
# # -------------------------------------------------------------------

@method_decorator(login_required, name='dispatch')
class JobApplyCreateView(CreateView):
    template_name = "page/job-apply.html"
    form_class = CareerManageForm

    def form_valid(self, form, **kwargs):
        # title = form.instance.title
        slug = self.kwargs['slug']
        job_qs = Job.objects.filter(slug=slug)
        if job_qs.exists():
            form.instance.user = self.request.user
            form.instance.job = job_qs.last()
            messages.add_message(
                self.request, messages.SUCCESS, "Applied successfully!"
            )
            return super().form_valid(form)
        messages.add_message(
            self.request, messages.ERROR, "Failed to apply!"
        )
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.POST.get('next', reverse('home'))

    def get_context_data(self, **kwargs):
        context = super(
            JobApplyCreateView, self
        ).get_context_data(**kwargs)
        context['page_title'] = 'Create Project Category'
        return context
