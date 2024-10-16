from django.urls import path
from rest_framework import routers

from .views import ProfileViewSet


def register_viewset(router: routers.DefaultRouter):
    router.register(r"profiles", ProfileViewSet, basename="profile")


urlpatterns = []
