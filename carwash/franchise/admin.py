from django.contrib import admin
from .models import City, Franchise, Services

# Register your models here.

from django.contrib import admin


class ServicesAdmin(admin.ModelAdmin):
    list_filter = ['services', 'city', 'franchise']
    search_fields = ['services', 'city__city', 'franchise__franchise']
# class MembershipInline(admin.TabularInline):
#     model = Franchise.members.through
#
#
# # class CityAdmin(admin.ModelAdmin):
# #     inlines = [
# #         MembershipInline,
# #     ]
#
#
# class FranchiseAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('members',)

admin.site.register(Franchise)
admin.site.register(City)
admin.site.register(Services, ServicesAdmin)
