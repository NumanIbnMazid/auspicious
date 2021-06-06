from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Import Views
from .views import  AboutView, \
    CivilServicesView, TelecomServicesView, ClientView, NewsView,\
    ContactView, NewsDetailsView, JobApplyCreateView

urlpatterns = [
    # path("", HomeView.as_view(), name="home"),
    path("", views.home, name="home"),
    path("apply/job/<slug>/", JobApplyCreateView.as_view(), name="job_apply"),
    path("about/", AboutView.as_view(), name="about"),
    path("civil-project/", views.civilproject, name="civil_project"),
    path("telecom-project/", views.telecomproject, name="telecom_project"),
    path("civil-service/", CivilServicesView.as_view(), name="civil_service"),
    path("telecom-service/", TelecomServicesView.as_view(), name="telecom_service"),
    path("career/", views.career, name="career"),
    path("all-job-list/", views.all_job_lists, name="all_job_lists"),
    path("jobs/<slug>/", views.filtered_job_lists, name="filtered_job_lists"),
    path("job-details/<slug>/", views.job_details, name="job_details"),
    path("sister & client/", ClientView.as_view(), name="client"),
    path("news/", NewsView.as_view(), name="news"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("news-details/", NewsDetailsView.as_view(), name="news_details"),
    path("admin/", admin.site.urls),
    path("account/", include("accounts.urls")),
    path("dashboard/", include(("dashboard.urls", "dashboard"), namespace="dashboard")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
