from django.urls import path
from .views import (
    DashboardView,
    ProjectCreateView, ProjectUpdateView, ProjectDetailView, delete_project, NewsCategoryCreateView,
    delete_news_category, NewsCategoryUpdateView, NewsCategoryDetailView
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
]
