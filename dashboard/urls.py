from django.urls import path
from .views import (
    DashboardView,
    ProjectCreateView, ProjectUpdateView, ProjectDetailView, delete_project
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
]
