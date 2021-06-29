from django.urls import path, include
from .views import (
    GroupCreateView, GroupUpdateView, GroupDetailView, delete_group,
    create_user, ProfileUpdateView, delete_user, UserDetailView,user_list,EndUserDetailView
)

urlpatterns = [
    # # ****************************** AllAuth ******************************
    path('', include('allauth.urls')),

    # # ****************************** Group ******************************
    path("create-group/", GroupCreateView.as_view(), name="create_group"),
    path("group/<id>/update/", GroupUpdateView.as_view(), name="update_group"),
    path("group/<id>/detail/", GroupDetailView.as_view(), name="group_detail"),
    path("delete-group/", delete_group, name="delete_group"),
    
    # # ****************************** User ******************************
    path("create-user/", create_user, name="create_user"),
    path("user/<slug>/update/", ProfileUpdateView.as_view(), name="update_user"),
    path("delete-user/", delete_user, name="delete_user"),
    path("user/<slug>/detail/", UserDetailView.as_view(), name="user_detail"),

# # ****************************** End User ******************************
    path("list-user/", user_list, name="list_user"),
    path("user/<slug>/detail/", EndUserDetailView.as_view(), name="user_details"),
]
