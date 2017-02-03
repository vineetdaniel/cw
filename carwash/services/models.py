from __future__ import unicode_literals

from django.db import models


class ServiceType(models.Model):
    service_name = models.CharField(max_length=20)

    class Meta:
        ordering = ('service_name', )

    def __unicode__(self):
        return '%s' % self.service_name


class ServiceNature(models.Model):
    CHOICES = (
        ('studio', 'Studio'),
        ('doorstep', 'Doorstep')
    )
    service_type = models.ForeignKey(ServiceType)
    service_location = models.CharField(max_length=20, choices=CHOICES)
    name = models.CharField(max_length=25)
    desc = models.TextField()
    #price = models.PositiveIntegerField()

    class Meta:
        ordering = ('name', )
        app_label = 'services'

    def __unicode__(self):
        return '%s %s' % (self.name, self.service_location)


