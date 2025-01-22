from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import HealthCheckEndpoint

app_name = 'temp'

router = DefaultRouter()

urlpatterns = [
    path('', HealthCheckEndpoint.as_view(), name="health-check"),
]
