from __future__ import unicode_literals

from django.db import models


class Vehicles(models.Model): # car, truck etc
    type = models.CharField(max_length=20, default='Car')

    class Meta:
        ordering = ('type', )


class VehicleType(models.Model): #SUV/Sedan
    type = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ('type', )

    def __unicode__(self):
        return '%s' % self.type


class Brand(models.Model):
    brand_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('brand_name', )

    def __unicode__(self):
        return '%s' % self.brand_name


class Model(models.Model):
    brand_id = models.ForeignKey(Brand)
    vehicle_id = models.ForeignKey(VehicleType, default=1)
    model_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('model_name', )

    def __unicode__(self):
        return '%s %s %s' % (self.brand_id, self.model_name,  self.vehicle_id)

