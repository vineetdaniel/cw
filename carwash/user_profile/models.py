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
    lat = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return u'%s profile' % self.user.username


class UserVehicles(models.Model):
    user = models.ForeignKey(User)
    reg_no = models.CharField(max_length=15)
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('modified', )






