#vehicle, vehicletype, model, brand
from rest_framework import serializers
from models import VehicleType, Vehicles, Model, Brand


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicles
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):

    class Meta:
        models = Model
        fields = '__all__'


