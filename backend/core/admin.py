from django.contrib import admin
from django.utils.html import format_html
from .models.components import OwnershipForm, Address, LegalEntity, Document
from .models.person import Person


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type', 'file')
    search_fields = ('title',)
    list_filter = ('document_type',)


@admin.register(OwnershipForm)
class OwnershipFormAdmin(admin.ModelAdmin):
    list_display = ['short_form', 'long_form']
    search_fields = ['short_form', 'long_form']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'district', 'street', 'house', 'flat', 'postal_code']
    search_fields = ['country', 'city', 'postal_code']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'date_of_birth', 'email', 'phone_number', 'age')
    search_fields = ('first_name', 'last_name', 'middle_name', 'email', 'phone_number')
    list_filter = ('date_of_birth',)


@admin.register(LegalEntity)
class LegalEntityAdmin(admin.ModelAdmin):
    list_display = ['name', 'ownership_form', 'address', 'phoneNumber', 'websiteUrl',
                    'logo_thumbnail']
    search_fields = ['name', 'phoneNumber', 'websiteUrl']

    # inlines = [EmployeeInline, CorporateDocumentInline]

    # def employees_list(self, obj):
    #     employees = obj.employee_set.all()
    #     return format_html('<br>'.join([str(employee) for employee in employees]))

    def logo_thumbnail(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="150" />'.format(obj.logo.url))
        return '-'

    # corporate_documents_list.short_description = 'Корпоративные документы'
    # employees_list.short_description = 'Сотрудники'
    logo_thumbnail.short_description = 'Логотип'
