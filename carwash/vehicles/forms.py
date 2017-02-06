import django_filters

from .models import Vehicles

class VehicleFilter(django_filters.FilterSet):

    class Meta:
        model = Vehicles
        fields = '__all__'