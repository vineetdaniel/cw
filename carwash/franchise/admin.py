from django.contrib import admin
from .models import City, Franchise, Services

# Register your models here.

from django.contrib import admin
from guardian.admin import GuardedModelAdmin


class ServicesAdmin(admin.ModelAdmin):
    list_filter = ['services', 'city', 'franchise']
    search_fields = ['services', 'city__city', 'franchise__franchise']


    def has_add_permission(self, request):
        # This one doesn't get an object to play with, because there is no
        # object yet, but you can still do things like:
        return request.user.is_superuser
        # This will allow only superusers to add new objects of this type


    def has_change_permission(self, request, obj=None):
        # Here you have the object, but this is only really useful if it has
        # ownership info on it, such as a `user` FK
        if obj is not None:
            return request.user.is_superuser or \
                   obj.user == request.user
            # Now only the "owner" or a superuser will be able to edit this object
        else:
            # obj == None when you're on the changelist page, so returning `False`
            # here will make the changelist page not even viewable, as a result,
            # you'd want to do something like:
            return request.user.is_superuser or \
                   self.model._default_manager.filter(user=request.user).exists()
            # Then, users must "own" *something* or be a superuser or they
            # can't see the changelist


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
