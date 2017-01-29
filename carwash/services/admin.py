from django.contrib import admin
from .models import ServiceNature, ServiceType


admin.site.register(ServiceType)
admin.site.register(ServiceNature)

# Register your models here.
