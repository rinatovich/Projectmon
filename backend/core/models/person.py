from datetime import date
from django.db import models


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
