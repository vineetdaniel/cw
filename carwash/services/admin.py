from django.contrib import admin
from .models import ServiceNature, ServiceType


admin.site.register(ServiceType)


class ServiceNatureAdmin(admin.ModelAdmin):
    list_filter = ['service_type', 'service_location']
    search_fields = ['name']

admin.site.register(ServiceNature, ServiceNatureAdmin)

# Register your models here.
