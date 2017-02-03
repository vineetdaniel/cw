from django.contrib import admin
from .models import Person, Group, Membership

# Register your models here.

from django.contrib import admin


class MembershipInline(admin.TabularInline):
    model = Group.members.through


class PersonAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


class GroupAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('members',)


admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Membership)