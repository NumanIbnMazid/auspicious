from django.views.generic import TemplateView
from dashboard.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import date, datetime, timedelta

# class HomeView(request):
#     project_category_qs = ProjectCategory.objects.all()
#     project_qs = Project.objects.all()
#     contex = {'project_category_qs':project_category_qs,
#               'project_qs':project_qs}
#
#     # template_name = "index.html"
#     return render(request, 'index.html', contex)
#

def home(request):
    today = timezone.datetime.now()
    datetime_today = datetime.strptime(
        str(today.date()) + " 00:00:00", '%Y-%m-%d %H:%M:%S'
    )
    project_category_qs = ProjectCategory.objects.all()
    project_lists = Project.objects.all()
    print(project_lists.count())
    ongoing_project_lists = Project.objects.filter(developement_start_year__lte = datetime_today.year,developement_end_year = None)
    completed_project_lists = Project.objects.filter(developement_start_year__lte = datetime_today.year,developement_end_year__lte = datetime_today.year)
    latest_project_lists = Project.objects.filter(developement_start_year__lte = datetime_today.year, created_at__lte = today.date())
    latest_news_category_lists = NewsCategory.objects.all()
    latest_news_lists = News.objects.all()
    context = {'project_category_qs':project_category_qs,
              'project_lists':project_lists,'ongoing_project_lists':ongoing_project_lists,
               'completed_project_lists':completed_project_lists,'latest_project_lists':latest_project_lists,
               'latest_news_category_lists':latest_news_category_lists,'latest_news_lists':latest_news_lists}

    return render(request, 'index.html', context)
#


class AboutView(TemplateView):
    template_name = 'page/about.html'

class CivilProjectView(TemplateView):
    template_name = 'page/civil-project.html'

class TelecomProjectView(TemplateView):
    template_name = 'page/telecom-project.html'

class CivilServicesView(TemplateView):
    template_name = 'page/civil-service.html'

class TelecomServicesView(TemplateView):
    template_name = 'page/telecom-service.html'

class CareerView(TemplateView):
    template_name = 'page/career.html'

class ClientView(TemplateView):
    template_name = 'page/client.html'

class NewsView(TemplateView):
    template_name = 'page/news.html'

class ContactView(TemplateView):
    template_name = 'page/contact.html'

class NewsDetailsView(TemplateView):
    template_name = 'page/news-details.html'
