from django.db import models
from services.models import ServiceNature
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Franchise(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(City, through='Services')
    address = models.TextField(blank=True)
    mobile_no = models.PositiveIntegerField(blank=True, null=True)
    landline_no = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    pincode = models.PositiveIntegerField(null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Services(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)
    services = models.ForeignKey(ServiceNature)
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateField(null=True)
    invite_reason = models.CharField(max_length=64, null=True)

    class Meta:
        unique_together = ('city', 'franchise', 'services', )
        permissions = (
            ('view_services', 'Can view'),
        )

    def __unicode__(self):
        return '%s - %s' % (self.franchise, self.services, )





# Create your models here.
