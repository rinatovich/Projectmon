# from django.core.validators import RegexValidator
# from django.db import models
# from core.models.entities import *
# from core.models.base import *
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
#
# from django.db import models
#
#
# class DeviceCategory(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Название категории')
#
#     class Meta:
#         verbose_name = "Категория устройства"
#         verbose_name_plural = "Категории устройств"
#
#     def __str__(self):
#         return self.name
#
#
# class Device(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Название')
#     description = models.TextField(verbose_name='Описание')
#     part_number = models.CharField(max_length=50, verbose_name='Парт номер')
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена',null=True, blank=True)
#     purpose = models.CharField(max_length=255, verbose_name='Назначение')
#     category = models.ForeignKey(DeviceCategory, on_delete=models.SET_NULL, null=True, blank=True,
#                                  verbose_name='Категория')
#     manufacturer = models.CharField(max_length=255, verbose_name='Производитель', blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_full_description(self):
#         return f"{self.name} - {self.description}. Цена: {self.price}"
#
#     def formatted_price(self):
#         return f"USD {self.price:.2f}"
#
#     class Meta:
#         verbose_name = "Устройство"
#         verbose_name_plural = "Устройства"
#
#
# class Item(models.Model):
#     equipment = models.ForeignKey('Device', on_delete=models.CASCADE, verbose_name='Оборудование')
#     quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
#     specification = models.ForeignKey('Specification', on_delete=models.CASCADE, verbose_name='Спецификация')
#
#     def __str__(self):
#         return f'{self.equipment}'
#
#     class Meta:
#         verbose_name = "Пункт"
#         verbose_name_plural = "Пункты"
#
#
# class Vendordoc(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название')
#     file = models.FileField(upload_to='media/vendordocs/', verbose_name='Файлы вендоров')
#     specification = models.ForeignKey('Specification', on_delete=models.CASCADE, verbose_name='Спецификация')
#
#     def __str__(self):
#         return f'{self.title}'
#
#     class Meta:
#         verbose_name = "Файл вендора"
#         verbose_name_plural = "Файлы вендоров"
#
#
# class Specification(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название')
#
#     def __str__(self):
#         return f'{self.title}'
#
#     class Meta:
#         verbose_name = "Спецификация"
#         verbose_name_plural = "Спецификации"
#
#
# class ProjectDocument(Document):
#     STATUS_CHOICES = (
#         ('draft', 'Черновик'),
#         ('approved', 'Утвержден'),
#         ('obsolete', 'Устарел'),
#     )
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
#     project_stage = models.ForeignKey('ProjectStage', on_delete=models.CASCADE, verbose_name='Этап проекта',
#                                       related_name='project_documents')
#
#     class Meta:
#         verbose_name = "Документ проекта"
#         verbose_name_plural = "Документ проекта"
#
#
# class ProjectStage(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название этапа')
#     start_date = models.DateField(verbose_name='Дата начала', blank=True, null=True)
#     end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
#     number = models.PositiveIntegerField(verbose_name='Номер этапа', blank=True, null=True, editable=False)
#     # Добавим поля для отслеживания прогресса
#     completed = models.BooleanField(default=False, verbose_name='Завершено')
#     project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name='Проект',
#                                 related_name='projectstages')
#
#     def save(self, *args, **kwargs):
#         if not self.number:
#             max_number = ProjectStage.objects.filter(project=self.project).aggregate(models.Max('number'))[
#                 'number__max']
#             self.number = max_number + 1 if max_number is not None else 1
#         super().save(*args, **kwargs)
#
#     class Meta:
#         verbose_name = "Этап проекта"
#         verbose_name_plural = "Этапы проекта"
#
#     def __str__(self):
#         return f'{self.number}. {self.title}'
#
#
# class TenderStage(ProjectStage):
#     link = models.URLField(verbose_name='ссылка на лот', blank=True, null=True)
#     lot = models.CharField(max_length=255, verbose_name='Лот', blank=True, null=True)
#
#     class Meta:
#         verbose_name = "Тендер"
#         verbose_name_plural = "Тендера"
#
#     def __str__(self):
#         return f'Лот № {self.lot}'
#
#
# @receiver(pre_save, sender=ProjectStage)
# def set_project_stage_number(sender, instance, **kwargs):
#     if not instance.number:
#         max_number = ProjectStage.objects.filter(project=instance.project).aggregate(models.Max('number'))[
#             'number__max']
#         instance.number = max_number + 1 if max_number is not None else 1
#
#
# class Project(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Название проекта')
#     customer = models.ForeignKey('LegalEntity', on_delete=models.CASCADE, verbose_name='Заказчик')
#     specification = models.ForeignKey('Specification', on_delete=models.CASCADE, verbose_name='Спецификация',
#                                       blank=True, null=True)
#
#     def get_documents(self):
#         documents = ProjectDocument.objects.filter(project_stage__project=self)
#         return documents
#
#     class Meta:
#         verbose_name = "Проект"
#         verbose_name_plural = "Проекты"
#
#     def __str__(self):
#         return f"{self.title}"
