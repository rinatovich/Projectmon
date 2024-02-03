from django.contrib import admin
from django.utils.html import format_html
from .models.base import *
from .models.entities import *
from .models.project import *


# _______________Persons Admin_______________
class PersonalDocumentInline(admin.TabularInline):
    model = PersonalDocument
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'date_of_birth', 'email', 'phone_number', 'display_age')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('date_of_birth',)
    ordering = ('last_name', 'first_name')
    inlines = [PersonalDocumentInline]

    actions = ['convert_to_employee']

    def convert_to_employee(self, request, queryset):
        for person in queryset:
            employee = Employee.objects.create(
                first_name=person.first_name,
                last_name=person.last_name,
                middle_name=person.middle_name,
                date_of_birth=person.date_of_birth,
                email=person.email,
                phone_number=person.phone_number,
                # Добавьте остальные поля Employee
            )
            # Удалите person, если нужно
            person.delete()

        self.message_user(request, f"Selected persons converted to employees.")

    convert_to_employee.short_description = "Превратить выбранных людей в сотрудников"

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'middle_name')
        }),
        ('Дополнительная информация', {
            'fields': ('date_of_birth', 'email', 'phone_number')
        }),
    )

    readonly_fields = ('age',)

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = 'Полное имя'

    def display_age(self, obj):
        return obj.age

    display_age.short_description = 'Возраст'


class EmployeeDocumentInline(admin.TabularInline):
    model = EmployeeDocument
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('get_full_name_with_job_title', 'date_of_birth', 'job_email', 'jobTitle', 'company', 'display_age')
    search_fields = ('first_name', 'last_name', 'email', 'job_email', 'jobTitle', 'company__name')
    list_filter = ('date_of_birth', 'company__name', 'jobTitle')
    ordering = ('last_name', 'first_name')
    inlines = [EmployeeDocumentInline]

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'middle_name')
        }),
        ('Личная информация', {
            'fields': ('date_of_birth', 'email', 'phone_number')
        }),
        ('Рабочая информация', {
            'fields': ('job_email', 'jobTitle', 'company')
        }),
    )

    readonly_fields = ('age',)

    def display_age(self, obj):
        return obj.age

    display_age.short_description = 'Возраст'


# _______________Persons Admin_______________


# _______________Components Admin_______________
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'city', 'district', 'street', 'house', 'flat', 'postal_code']
    search_fields = ['country', 'city', 'postal_code']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type', 'created_at', 'modified_at')
    search_fields = ('title', 'document_type')
    list_filter = ('document_type', 'created_at', 'modified_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'modified_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'document_type', 'file')
        }),
        ('Важные даты', {
            'fields': ('created_at', 'modified_at'),
        }),
    )


@admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(DocumentAdmin):
    list_display = ('title', 'document_type', 'created_at', 'modified_at', 'employee')


@admin.register(PersonalDocument)
class PersonalDocumentAdmin(DocumentAdmin):
    list_display = ('title', 'document_type', 'created_at', 'modified_at', 'person')


@admin.register(OwnershipForm)
class OwnershipFormAdmin(admin.ModelAdmin):
    list_display = ['shortForm', 'longForm']
    search_fields = ['shortForm', 'longForm']


class DetailFieldInline(admin.TabularInline):
    model = DetailField
    extra = 1


@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['detailfields_list']
    inlines = [DetailFieldInline]

    def detailfields_list(self, obj):
        detailfields = obj.detailfield_set.all()
        return format_html('<br>'.join([str(detailfield) for detailfield in detailfields]))

    detailfields_list.short_description = 'Сотрудники'


# _______________Components Admin_______________


# _______________Entities Admin_______________
class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 1
    verbose_name_plural = 'Сотрудники'
    can_delete = True


@admin.register(CorporateDocument)
class CorporateDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type', 'legal_entity', 'created_at', 'modified_at')
    search_fields = ('title', 'document_type', 'legal_entity__name')
    list_filter = ('document_type', 'legal_entity', 'created_at', 'modified_at')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'modified_at')

    fieldsets = (
        (None, {
            'fields': ('title', 'document_type', 'file', 'legal_entity')
        }),
        ('Важные даты', {
            'fields': ('created_at', 'modified_at'),
        }),
    )


class CorporateDocumentInline(admin.StackedInline):
    model = CorporateDocument
    extra = 1
    readonly_fields = ('created_at', 'modified_at')


@admin.register(LegalEntity)
class LegalEntityAdmin(admin.ModelAdmin):
    list_display = ['name', 'ownershipForm', 'address', 'details', 'phoneNumber', 'websiteUrl', 'employees_list',
                    'logo_thumbnail']
    search_fields = ['name', 'phoneNumber', 'websiteUrl']
    inlines = [EmployeeInline, CorporateDocumentInline]

    def employees_list(self, obj):
        employees = obj.employee_set.all()
        return format_html('<br>'.join([str(employee) for employee in employees]))

    def logo_thumbnail(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="150" />'.format(obj.logo.url))
        return '-'

    # corporate_documents_list.short_description = 'Корпоративные документы'
    employees_list.short_description = 'Сотрудники'
    logo_thumbnail.short_description = 'Логотип'


@admin.register(Organization)
class OrganizationAdmin(LegalEntityAdmin):
    list_display = ['name', 'ownershipForm', 'address', 'details', 'phoneNumber', 'websiteUrl', 'logo_thumbnail',
                    'serviceBank_display', 'employees_list']
    search_fields = ['name', 'phoneNumber', 'websiteUrl']

    def serviceBank_display(self, obj):
        return obj.serviceBank  # Display the related Bank object

    serviceBank_display.short_description = 'Обслуживающий банк'


@admin.register(Bank)
class BankAdmin(LegalEntityAdmin):
    list_display = ['name', 'ownershipForm', 'address', 'details', 'phoneNumber', 'websiteUrl', 'logo_thumbnail']
    search_fields = ['name', 'phoneNumber', 'websiteUrl']


# _______________Entities Admin_______________


# _______________Project Admin_______________
@admin.register(DeviceCategory)
class DeviceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'formatted_price')
    search_fields = ('name', 'category__name', 'price')
    list_filter = ('category',)
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'part_number', 'price', 'purpose', 'category', 'manufacturer')
        }),
    )

    readonly_fields = ('formatted_price', 'get_full_description')

    def get_full_description(self, obj):
        return obj.get_full_description()

    get_full_description.short_description = 'Полное описание'

    def formatted_price(self, obj):
        return obj.formatted_price()

    formatted_price.short_description = 'Цена (USD)'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'quantity', 'specification')
    search_fields = ('equipment__name', 'specification__title')
    list_filter = ('specification',)
    ordering = ('equipment__name',)


@admin.register(Vendordoc)
class VendordocAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    ordering = ('title',)


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class VendordocInline(admin.TabularInline):
    model = Vendordoc
    extra = 1


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'items_list', 'vendordocs_list')
    search_fields = ('title',)
    ordering = ('title',)

    inlines = [ItemInline, VendordocInline]

    def items_list(self, obj):
        items = obj.item_set.all()
        return format_html('<br>'.join([str(item) for item in items]))

    def vendordocs_list(self, obj):
        vendordocs = obj.item_set.all()
        return format_html('<br>'.join([str(vendordoc) for vendordoc in vendordocs]))

    vendordocs_list.short_description = 'Устройства'
    items_list.short_description = 'Устройства'


@admin.register(ProjectDocument)
class ProjectDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'project_stage', 'created_at')
    list_filter = ('status', 'project_stage__project', 'created_at')
    search_fields = ('title', 'project_stage__title')

    def get_queryset(self, request):
        # Оптимизация запроса для связанного поля
        return super().get_queryset(request).select_related('project_stage__project')


class ProjectDocumentInline(admin.TabularInline):
    model = ProjectDocument
    extra = 1


@admin.register(ProjectStage)
class ProjectStageAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'start_date', 'end_date', 'completed', 'project', 'created_at', 'number', 'projectdocuments_list')
    list_filter = ('completed', 'project', 'created_at')

    inlines = [ProjectDocumentInline]

    def projectdocuments_list(self, obj):
        projectdocuments = obj.project_documents.all()
        return format_html('<br>'.join([str(projectdocument) for projectdocument in projectdocuments]))

    projectdocuments_list.short_description = 'Документы проекта'


@admin.register(TenderStage)
class TenderStageAdmin(ProjectStageAdmin):
    list_display = (
        'title', 'start_date', 'end_date', 'completed', 'project', 'created_at', 'number', 'projectdocuments_list', 'link', 'lot')
    list_filter = ('completed', 'project', 'created_at')

    inlines = [ProjectDocumentInline]

    def projectdocuments_list(self, obj):
        projectdocuments = obj.project_documents.all()
        return format_html('<br>'.join([str(projectdocument) for projectdocument in projectdocuments]))

    projectdocuments_list.short_description = 'Документы проекта'



class ProjectStageInline(admin.TabularInline):
    model = ProjectStage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'specification', 'projectstages_list', 'display_documents')
    search_fields = ('title', 'customer__name', 'specification__title')
    list_filter = ('customer', 'specification')
    ordering = ('title',)

    inlines = [ProjectStageInline]  # Замените ProjectStageAdmin на ProjectStageInline

    def projectstages_list(self, obj):
        projectstages = obj.projectstages.all()  # Обновите projectstages_set на projectstages
        return format_html('<br>'.join([str(projectstage) for projectstage in projectstages]))

    def display_documents(self, obj):
        documents = obj.get_documents()
        return ', '.join([str(document) for document in documents])

    display_documents.short_description = 'Документы'

    projectstages_list.short_description = 'Этапы'
# _______________Project Admin_______________
