from rest_framework import status, viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileViewSet(
    CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get("email")
        if email:
            request.data["email"] = email.lower()

        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
