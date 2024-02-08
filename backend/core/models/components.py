from django.core.validators import RegexValidator
from django.db import models


class Document(models.Model):
    DOC_TYPES = (
        ('word', 'Word'),
        ('excel', 'Excel'),
        ('powerpoint', 'PowerPoint'),
        ('pdf', 'PDF'),
        ('visio', 'Visio'),
    )

    title = models.CharField(max_length=255, verbose_name='Название документа')
    document_type = models.CharField(max_length=20, choices=DOC_TYPES, verbose_name='Тип документа')
    file = models.FileField(upload_to='documents/', verbose_name='Файл')

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.title


class OwnershipForm(models.Model):
    short_form = models.CharField(max_length=255, verbose_name='короткая форма')
    long_form = models.CharField(max_length=255, verbose_name='длинная форма')

    class Meta:
        verbose_name = "Форма принадлежности"
        verbose_name_plural = "Формы принадлежности"

    def __str__(self):
        return f"{self.short_form}"


class Address(models.Model):
    country = models.CharField(max_length=255, verbose_name='Страна', default='Узбекистан')
    city = models.CharField(max_length=255, verbose_name='Город', default='Ташкент')
    district = models.CharField(max_length=255, verbose_name='Район', blank=True, null=True, default='')
    street = models.CharField(max_length=255, verbose_name='Улица', blank=True, null=True, default='')
    house = models.CharField(max_length=255, verbose_name='Дом', blank=True, null=True, default='')
    flat = models.CharField(max_length=255, verbose_name='Квартира', blank=True, null=True, default='')
    postal_code = models.CharField(max_length=10, verbose_name='Индекс')

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return f"Улица: {self.street}, дом: {self.house}, Индекс: {self.postal_code}"

    def get_full_address(self):
        address_parts = [self.country, f"город {self.city}, {self.postal_code},"]

        if self.district:
            address_parts.append(self.district)

        if self.street:
            address_parts.append(f"ул. {self.street}")

        if self.house:
            address_parts.append(f"{self.house}")

        if self.flat:
            address_parts.append(f", квартира {self.flat}")

        return ", ".join(address_parts)


class LegalEntity(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    ownership_form = models.ForeignKey('OwnershipForm', on_delete=models.CASCADE, verbose_name='Форма принадлежности')
    address = models.ForeignKey('Address', on_delete=models.CASCADE, verbose_name='Адрес')
    # details = models.ForeignKey('Details', on_delete=models.CASCADE, verbose_name='Реквизиты')
    phoneNumber = models.CharField(max_length=15,
                                   validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Invalid phone number")],
                                   verbose_name='Номер телефона', blank=True, null=True)
    websiteUrl = models.URLField(verbose_name='ссылка на сайт', blank=True, null=True)
    logo = models.ImageField(upload_to='organizations/logos/', verbose_name='Логотип компании', blank=True, null=True)

    class Meta:
        verbose_name = "Юридическое лицо"
        verbose_name_plural = "Юридические лица"

    def __str__(self):
        return f"{self.name}"


