from rest_framework import serializers
from models import Profile, UserVehicles, User


class ProfileSerializer(serializers.ModelSerializer):
   # vehicles = VehiclesSerializers(many=True)

    class Meta:
        model = Profile
        fields = '__all__'


class VehiclesSerializers(serializers.ModelSerializer):
    profile = ProfileSerializer(many=True, read_only=True)

    class Meta:
        model = UserVehicles
        fields = ('model', 'brand', 'type', 'profile',)


