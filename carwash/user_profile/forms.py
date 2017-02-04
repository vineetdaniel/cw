import django_filters

from .models import UserVehicles

class VehicleFilter(django_filters.FilterSet):

    class Meta:
        model = UserVehicles
        fields = ('model', )