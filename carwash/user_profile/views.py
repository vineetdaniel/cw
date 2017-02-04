from models import Profile, UserVehicles
from rest_framework import generics

from .serializers import ProfileSerializer, VehiclesSerializers


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserVehiclesView(generics.RetrieveAPIView):
    queryset = UserVehicles.objects.all()
    serializer_class = VehiclesSerializers




