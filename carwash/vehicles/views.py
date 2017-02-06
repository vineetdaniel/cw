from models import Vehicles, VehicleType, Brand, Model
from rest_framework import generics, filters, viewsets
from .serializers import VehicleSerializer, VehicleTypeSerializer, VehicleBrandSerializer, VehicleModelSerializer
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


class VehicleDetailView(generics.RetrieveAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer


class VehicleViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer
    # filter_class = VehicleFilter
    # search_fields = ('brand', 'user__user',)
    # ordering_fields = ('brand', )


class VehicleTypeViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleBrandViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = VehicleBrandSerializer


class VehicleModelViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = VehicleModelSerializer
