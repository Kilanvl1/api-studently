from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin

from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileViewSet(CreateModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.none()
    serializer_class = ProfileSerializer
