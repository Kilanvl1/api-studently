from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileViewSet(generics.CreateAPIView, viewsets.GenericViewSet):
    serializer_class = ProfileSerializer
