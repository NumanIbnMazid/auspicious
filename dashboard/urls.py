from django.urls import path
from .views import (
    DashboardView,
    ProjectCategoryDetailView,ProjectCreateView, ProjectUpdateView, ProjectDetailView, delete_project, NewsCategoryCreateView,
    delete_news_category, NewsCategoryUpdateView, NewsCategoryDetailView, NewsCreateView, NewsDetailView,
    NewsUpdateView, delete_news, GalleryCreateView, GalleryDetailView, GalleryUpdateView, delete_gallery,
    ClientCreateView, ClientUpdateView, ClientDetailView, delete_client, SocialAccountCreateView,
    SocialAccountUpdateView, SocialAccountDetailView, delete_social_account, delete_job_position, JobPositionCreateView,
    JobPositionUpdateView, JobPositionDetailView, ContactCreateView, ContactUpdateView, ContactDetailView,
    delete_contact, ProjectCategoryCreateView, ProjectCategoryUpdateView, delete_project_category,
    JobCreateView, JobUpdateView, JobDetailView, delete_job,
    JobApplicationListView, JobApplicationUpdateView, JobApplicationDetailView, delete_job_application,
    update_job_application_status,
    CVListView, CVUpdateView, delete_cv, CVDetailView
)



urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),

    # # -------------------------------------------------------------------
    # #                              Project Category
    # # -------------------------------------------------------------------
    path("create/project_category/", ProjectCategoryCreateView.as_view(),
         name="create_project_category"),
    path("update/project_category/<id>/",
         ProjectCategoryUpdateView.as_view(), name="update_project_category"),
    path("project_category/<id>/detail/",
         ProjectCategoryDetailView.as_view(), name="project_category_detail"),
    path("delete/project_category/", delete_project_category,
         name="delete_project_category"),

    # # -------------------------------------------------------------------
    # #                              Project
    # # -------------------------------------------------------------------
    path("create/project/", ProjectCreateView.as_view(),
         name="create_project"),
    path("update/project/<slug>/",
         ProjectUpdateView.as_view(), name="update_project"),
    path("project/<slug>/detail/",
         ProjectDetailView.as_view(), name="project_detail"),
    path("delete/project/", delete_project,
         name="delete_project"),
    # # -------------------------------------------------------------------
    # #                              News Category
    # # -------------------------------------------------------------------
    path("create/news_category/", NewsCategoryCreateView.as_view(),
         name="create_news_category"),
    path("update/news_category/<slug>/",
         NewsCategoryUpdateView.as_view(), name="update_news_category"),
    path("news_category/<slug>/detail/",
         NewsCategoryDetailView.as_view(), name="news_category_detail"),
    path("delete/news_category/", delete_news_category,
         name="delete_news_category"),
    # # -------------------------------------------------------------------
    # #                              News
    # # -------------------------------------------------------------------
    path("create/news/", NewsCreateView.as_view(),
         name="create_news"),
    path("update/news/<slug>/",
         NewsUpdateView.as_view(), name="update_news"),
    path("news/<slug>/detail/",
         NewsDetailView.as_view(), name="news_detail"),
    path("news/project/", delete_news,
         name="delete_news"),

    # # -------------------------------------------------------------------
    # #                              Gallery
    # # -------------------------------------------------------------------
    path("create/gallery/", GalleryCreateView.as_view(),
         name="create_gallery"),
    path("update/gallery/<slug>/",
         GalleryUpdateView.as_view(), name="update_gallery"),
    path("gallery/<slug>/detail/",
         GalleryDetailView.as_view(), name="gallery_detail"),
    path("news/gallery/", delete_gallery,
         name="delete_gallery"),

    # # -------------------------------------------------------------------
    # #                              Client
    # # -------------------------------------------------------------------
    path("create/client/", ClientCreateView.as_view(),
         name="create_client"),
    path("update/client/<slug>/",
         ClientUpdateView.as_view(), name="update_client"),
    path("client/<slug>/detail/",
         ClientDetailView.as_view(), name="client_detail"),
    path("news/client/", delete_client,
         name="delete_client"),

    # # -------------------------------------------------------------------
    # #                              Social Account
    # # -------------------------------------------------------------------
    path("create/social_account/", SocialAccountCreateView.as_view(),
         name="create_social_account"),
    path("update/social_account/<id>/",
         SocialAccountUpdateView.as_view(), name="update_social_account"),
    path("social_account/<id>/detail/",
         SocialAccountDetailView.as_view(), name="social_account_detail"),
    path("news/social_account/", delete_social_account,
         name="delete_social_account"),

    # # -------------------------------------------------------------------
    # #                              Job Position
    # # -------------------------------------------------------------------
    path("create/job_position/", JobPositionCreateView.as_view(),
         name="create_job_position"),
    path("update/job_position/<slug>/",
         JobPositionUpdateView.as_view(), name="update_job_position"),
    path("job_position/<slug>/detail/",
         JobPositionDetailView.as_view(), name="job_position_detail"),
    path("news/job_position/", delete_job_position,
         name="delete_job_position"),

    # # -------------------------------------------------------------------
    # #                              Job
    # # -------------------------------------------------------------------
    path("create/job/", JobCreateView.as_view(),
         name="create_job"),
    path("update/job/<slug>/",
         JobUpdateView.as_view(), name="update_job"),
    path("job/<slug>/detail/",
         JobDetailView.as_view(), name="job_detail"),
    path("news/job/", delete_job,
         name="delete_job"),

    # # -------------------------------------------------------------------
    # #                              Contact
    # # -------------------------------------------------------------------
    path("create/contact/", ContactCreateView.as_view(),
         name="create_contact"),
    path("update/contact/<id>/",
         ContactUpdateView.as_view(), name="update_contact"),
    path("contact/<id>/detail/",
         ContactDetailView.as_view(), name="contact_detail"),
    path("delete/contact/", delete_contact,
         name="delete_contact"),

    # # -------------------------------------------------------------------
    # #                       Career / Job Application
    # # -------------------------------------------------------------------
    path("job/application/list/", JobApplicationListView.as_view(),
         name="job_application_list"),
    path("job/application/<slug>/update/", JobApplicationUpdateView.as_view(),
         name="job_application_update"),
    path("job/application/<slug>/detail/",
         JobApplicationDetailView.as_view(), name="job_application_detail"),
    path("delete/job-application/", delete_job_application,
         name="delete_job_application"),
    path("update/job-application/<slug>/status", update_job_application_status,
         name="update_job_application_status"),

    # # -------------------------------------------------------------------
    # #                       Career / CV
    # # -------------------------------------------------------------------
    path("cv/list/", CVListView.as_view(),
         name="cv_list"),
    path("cv/<slug>/update/", CVUpdateView.as_view(),
         name="cv_update"),
    path("cv/<slug>/detail/",
         CVDetailView.as_view(), name="cv_detail"),
    path("delete/cv/", delete_cv,
         name="delete_cv"),
#     path("update/cv/<slug>/status", update_cv_status,
#          name="update_cv_status"),
]

