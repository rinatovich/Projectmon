from django.contrib import admin

# Register your models here.
from core.admin import PersonAdmin
from organization.models import *


@admin.register(Employee)
class EmployeeAdmin(PersonAdmin):
    list_display = ('get_full_name', 'date_of_birth', 'age', 'employer', )
    search_fields = ('first_name', 'last_name', 'middle_name', 'email', 'phone_number')
    list_filter = ('date_of_birth', 'employer')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title', 'ownership_form', 'address', 'phoneNumber', 'websiteUrl', 'logo')
    list_filter = ('ownership_form',)
    search_fields = ('title',)
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return '<img src="{url}" width="100px" height="auto" />'.format(url=obj.logo.url)
        else:
            return 'No logo'
    logo_preview.allow_tags = True