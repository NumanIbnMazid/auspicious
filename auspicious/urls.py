from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Import Views
from .views import  (AboutView,
    CivilServicesView, TelecomServicesView,
    JobApplyCreateView, JobApplyUpdateView,
    CivilServicesView, TelecomServicesView,
    JobApplyCreateView,CvDropCreateView,CvDropUpdateView,
    post_contact
)
from django.conf.urls import handler404

urlpatterns = [
    # path("", HomeView.as_view(), name="home"),
    path("", views.home, name="home"),
    path("apply/job/<slug>/", JobApplyCreateView.as_view(), name="job_apply"),
    path("cv-drop/", CvDropCreateView.as_view(), name="cv_drop"),
    path("apply/job/<slug>/update/", JobApplyUpdateView.as_view(), name="job_apply_update"),
    path("cv-drop/<slug>/update/", CvDropUpdateView.as_view(), name="cv_drop_update"),
    path("about/", AboutView.as_view(), name="about"),
    path("gallery/", views.gallery, name="gallery"),
    path("project_details/<slug>/", views.project_details, name="project_details"),
    path("civil-project/", views.civilproject, name="civil_project"),
    path("telecom-project/", views.telecomproject, name="telecom_project"),
    path("civil-service/", CivilServicesView.as_view(), name="civil_service"),
    path("telecom-service/", TelecomServicesView.as_view(), name="telecom_service"),
    path("career/", views.career, name="career"),
    path("all-job-list/", views.all_job_lists, name="all_job_lists"),
    path("jobs/<slug>/", views.filtered_job_lists, name="filtered_job_lists"),
    path("job-details/<slug>/", views.job_details, name="job_details"),
    # path("sister & client/", ClientView.as_view(), name="client"),
    path("sister-&-client/",views.client, name="client"),
    # path("news/", NewsView.as_view(), name="news"),
    path("news/", views.news, name="news"),
    path("news-category/<str:slug>/", views.filtered_news_lists, name="filtered_news_lists"),
    # path("contact/", ContactView.as_view(), name="contact"),
    path("contact/", views.contact, name="contact"),
    path("contact/post/", views.post_contact, name="post_contact"),
    path("news-details/<str:slug>/", views.news_details, name="news_details"),
    path("comment/<id>/reply/", views.comment_reply, name="comment_reply"),
    path("admin/", admin.site.urls),
    path("account/", include("accounts.urls")),
    path("dashboard/", include(("dashboard.urls", "dashboard"), namespace="dashboard")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

handler404 = 'auspicious.views.get_404_page'


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
