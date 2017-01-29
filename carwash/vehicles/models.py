from __future__ import unicode_literals

from django.db import models


class Vehicles(models.Model): # car, truck etc
    type = models.CharField(max_length=20, default='Car')

    class Meta:
        ordering = ('type', )


class VehicleType(models.Model): #SUV/Sedan
    type = models.CharField(max_length=20)

    class Meta:
        ordering = ('type', )


class Brand(models.Model):
    brand_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('brand_name', )


class Model(models.Model):
    brand_id = models.ForeignKey(Brand, related_name='brand_model')
    model_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('model_name', )