from django.db import models

# Create your models here.
from core.models.components import LegalEntity
from core.models.person import Person


class Employee(Person):
    email = models.EmailField(max_length=255, verbose_name='Электронная почта', blank=True, null=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', blank=True, null=True)
    employer = models.ForeignKey(LegalEntity, on_delete=models.CASCADE, verbose_name='Организация сотрудника')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.first_name}"


class Organization(LegalEntity):
    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return f"{self.title} (Организация)"
