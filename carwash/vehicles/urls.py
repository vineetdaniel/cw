from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

vehicles = DefaultRouter()
vehicles.register(r'vehicles', views.VehicleViewSet)
vehicles.register(r'brand', views.VehicleBrandViewSet)
vehicles.register(r'type', views.VehicleTypeViewSet)
vehicles.register(r'model', views.VehicleModelViewSet)
