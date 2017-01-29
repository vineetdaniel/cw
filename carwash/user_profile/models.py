from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# State :
# City:
# Pincode:
# Country:
#
# Car Brand
# Car Modal
# Car Type (Auto Fill according to car modal)
#
# Optional Fields : Assuming a person can have more than one car
# car Month/Year
# Car Km. Run
# Upload Photos (4 max)


class Profile(models.Model):
    GENDERS = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.OneToOneField(User, unique=True)
    gender = models.CharField(max_length=20, null=True, blank=True,
                              choices=GENDERS)
    city = models.CharField(max_length=250, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    locale = models.CharField(max_length=10, blank=True, null=True)
    ip = models.GenericIPAddressField()
    link = models.URLField()
    profile_picture = models.URLField(default='laskdfj')
    photo_id_front = models.ImageField(default='pic_folder/None/no-img')
    photo_id_back = models.ImageField(default='pic_folder/None/no-img')
    mobile_no = models.IntegerField(default=9999)
    UUID = models.UUIDField()

    def __unicode__(self):
        return u'%s profile' % self.user.username
