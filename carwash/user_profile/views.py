from models import Profile, UserVehicles
from rest_framework import generics, filters, viewsets
from .serializers import ProfileSerializer, VehiclesSerializers
from .forms import VehicleFilter


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
     and pagination."""

    # authentication_classes = (
    #     authentication.BasicAuthentication,
    #     authentication.TokenAuthentication,
    # )
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserVehiclesViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = UserVehicles.objects.all()
    serializer_class = VehiclesSerializers
    filter_class = VehicleFilter
    search_fields = ('brand', 'user__user',)
    ordering_fields = ('brand', )

# class UserVehiclesView(generics.RetrieveAPIView):
#     queryset = UserVehicles.objects.all()
#     serializer_class = VehiclesSerializers




