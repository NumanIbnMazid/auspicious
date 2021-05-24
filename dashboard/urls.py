from django.urls import path
from .views import (
    DashboardView,
    ProjectCreateView, ProjectUpdateView, ProjectDetailView, delete_project, NewsCategoryCreateView,
    delete_news_category, NewsCategoryUpdateView, NewsCategoryDetailView, NewsCreateView, NewsDetailView,
    NewsUpdateView, delete_news, GalleryCreateView, GalleryDetailView, GalleryUpdateView, delete_gallery
)




urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
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
    path("update/news_category/<id>/",
         NewsCategoryUpdateView.as_view(), name="update_news_category"),
    path("news_category/<id>/detail/",
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
]
