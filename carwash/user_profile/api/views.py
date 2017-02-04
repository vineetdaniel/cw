from models import Profile
from rest_framework import generics

from carwash.user_profile.serializers import ProfileSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


