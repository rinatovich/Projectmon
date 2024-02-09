from django.contrib import admin

# Register your models here.
from organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'ownership_form', 'address', 'phoneNumber', 'websiteUrl', 'logo')
    list_filter = ('ownership_form',)
    search_fields = ('name',)
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return '<img src="{url}" width="100px" height="auto" />'.format(url=obj.logo.url)
        else:
            return 'No logo'
    logo_preview.allow_tags = True