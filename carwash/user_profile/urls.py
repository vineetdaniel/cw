from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^account/(?P<pk>\d+)/$',
        views.ProfileDetailView.as_view(),
        name='profile_detail'),
    url(r'^account/vehicles/(?P<pk>\d+)/$',
        views.UserVehiclesView.as_view(),
        name='vehicle_detail'),
]