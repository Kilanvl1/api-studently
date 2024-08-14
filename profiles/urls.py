from django.urls import path
from rest_framework import routers

from .views import IncrementPageVisitsView, ProfileViewSet


def register_viewset(router: routers.DefaultRouter):
    router.register(r"profiles", ProfileViewSet, basename="profile")


urlpatterns = [
    path(
        "profile/<int:pk>/increment-page-visits/",
        IncrementPageVisitsView.as_view(),
        name="increment-page-visits",
    )
]
