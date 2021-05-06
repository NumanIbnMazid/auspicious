from django.urls import path
from .views import (
    DashboardView
)

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('create/news-category/', DashboardView.as_view(),
         name="create_news_category"),
]