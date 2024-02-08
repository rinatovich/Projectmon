# from django.core.validators import RegexValidator
# from django.db import models
#
# from core.models.base import *
# from core.models.components import *
# from core.models.project import *
#
#
# class Employee(Person):
#     job_email = models.EmailField(verbose_name='Рабочий E-mail', blank=True, null=True)
#     jobTitle = models.CharField(max_length=255, verbose_name='Должность', blank=True, null=True)
#     company = models.ForeignKey('LegalEntity', on_delete=models.CASCADE, verbose_name='Компания', blank=True,
#                                 null=True)
#
#     def get_full_name_with_job_title(self):
#         if self.middle_name and self.last_name and self.first_name:
#             full_name = f"{self.last_name} {self.first_name} {self.middle_name}"
#         elif self.last_name and self.first_name:
#             full_name = f"{self.first_name} {self.last_name}"
#         elif self.middle_name and self.first_name:
#             full_name = f"{self.first_name} {self.middle_name}"
#         else:
#             full_name = f"{self.first_name}"
#
#         if self.jobTitle:
#             full_name += f", {self.jobTitle}"
#
#         return full_name
#
#     def get_employee_info(self):
#         employee_info = {
#             'Имя': self.first_name if self.first_name else None,
#             'Фамилия': self.last_name if self.last_name else None,
#             'Отчество': self.middle_name if self.middle_name else None,
#             'Дата рождения': str(self.date_of_birth) if self.date_of_birth else None,
#             'Возраст': self.age,
#             'Электронная почта': self.email if self.email else None,
#             'Номер телефона': self.phone_number if self.phone_number else None,
#             'Рабочий E-mail': self.job_email if self.job_email else None,
#             'Должность': self.jobTitle if self.jobTitle else None,
#             'Компания': str(self.company) if self.company else None,
#         }
#         return employee_info
#
#     class Meta:
#         verbose_name = "Сотрудник"
#         verbose_name_plural = "Сотрудники"
#
#     def __str__(self):
#         return f"{super().get_full_name()} - {self.jobTitle} at {self.company}" if self.jobTitle and self.company else super().__str__()
#
#
# class EmployeeDocument(Document):
#     employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='Сотрудник')
#
#     class Meta:
#         verbose_name = "Документ сотрудника"
#         verbose_name_plural = "Документы сотрудников"
#
#
# class CorporateDocument(Document):
#     legal_entity = models.ForeignKey('LegalEntity', on_delete=models.CASCADE, verbose_name='Организация',
#                                      related_name='corporate_documents')
#
#     class Meta:
#         verbose_name = "Корпоративный документ"
#         verbose_name_plural = "Корпоративные документы"
#
#
# class LegalEntity(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Название')
#     ownership_form = models.ForeignKey('OwnershipForm', on_delete=models.CASCADE, verbose_name='Форма принадлежности')
#     address = models.ForeignKey('Address', on_delete=models.CASCADE, verbose_name='Адрес')
#     details = models.ForeignKey('Details', on_delete=models.CASCADE, verbose_name='Реквизиты')
#     phoneNumber = models.CharField(max_length=15,
#                                    validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Invalid phone number")],
#                                    verbose_name='Номер телефона', blank=True, null=True)
#     websiteUrl = models.URLField(verbose_name='ссылка на сайт', blank=True, null=True)
#     logo = models.ImageField(upload_to='organizations/logos/', verbose_name='Логотип компании', blank=True, null=True)
#
#     class Meta:
#         verbose_name = "Юридическое лицо"
#         verbose_name_plural = "Юридические лица"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Organization(LegalEntity):
#     serviceBank = models.ForeignKey('Bank', on_delete=models.CASCADE, verbose_name='Обслуживающий банк', blank=True,
#                                     null=True)
#
#     class Meta:
#         verbose_name = "Организация"
#         verbose_name_plural = "Организации"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Bank(LegalEntity):
#     pass
#
#     class Meta:
#         verbose_name = "Банк"
#         verbose_name_plural = "Банки"
#
#     def __str__(self):
#         return f"{self.name}"
