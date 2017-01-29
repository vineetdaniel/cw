from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Locations(models.Model):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    pincode = models.PositiveIntegerField()
    latitude = models.DecimalField(decimal_places=2, max_digits=10)
    longitude = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateTimeField()

    class Meta:
        ordering = ('pincode', 'city', )