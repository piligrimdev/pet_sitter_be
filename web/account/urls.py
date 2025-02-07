from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserDetailsView


urlpatterns = [
    path('user_details/', UserDetailsView.as_view(), name="user_details"),
]
