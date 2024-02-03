from django.core.validators import RegexValidator
from django.db import models
from datetime import date


class Person(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name='Электронная почта', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        if self.middle_name and self.last_name and self.first_name:
            return f"{self.last_name} {self.first_name} {self.middle_name}"
        if self.last_name and self.first_name:
            return f"{self.first_name} {self.last_name}"
        if self.middle_name and self.first_name:
            return f"{self.first_name} {self.middle_name}"
        else:
            return f"{self.first_name}"

    def get_all_data(self):
        data_with_labels = {
            'Имя': self.first_name if self.first_name else None,
            'Фамилия': self.last_name if self.last_name else None,
            'Отчество': self.middle_name if self.middle_name else None,
            'Дата рождения': str(self.date_of_birth) if self.date_of_birth else None,
            'Электронная почта': self.email if self.email else None,
            'Номер телефона': self.phone_number if self.phone_number else None,
        }
        return data_with_labels

    @property
    def age(self):
        today = date.today()
        birth_date = self.date_of_birth

        if birth_date:
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        else:
            return None


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


class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = (
        ('Файлы PDF', 'pdf'),
        ('Таблицы экзель', 'excel'),
        ('Документы', 'word'),
        ('Схемы', 'visio'),
        ('Презентации', 'pptx'),
        # Добавьте другие типы документов при необходимости
    )
    document_type = models.CharField(max_length=30, choices=DOCUMENT_TYPE_CHOICES, verbose_name='Тип документа')
    title = models.CharField(max_length=255, verbose_name='Название документа')
    file = models.FileField(upload_to='media/documents/', verbose_name='Файл документа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"


class PersonalDocument(Document):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Персона')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Персональный документ"
        verbose_name_plural = "Персональные документы"
