from core.models.base import *
from core.models.project import *


class OwnershipForm(models.Model):
    shortForm = models.CharField(max_length=255, verbose_name='короткая форма')
    longForm = models.CharField(max_length=255, verbose_name='длинная форма')

    class Meta:
        verbose_name = "Форма принадлежности"
        verbose_name_plural = "Формы принадлежности"

    def __str__(self):
        return f"{self.shortForm}"


class DetailField(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    value = models.CharField(max_length=255, verbose_name='Значение', blank=True, null=True)
    detail = models.ForeignKey('Details', on_delete=models.CASCADE, verbose_name='Реквизиты')

    class Meta:
        verbose_name = "Поле реквизита"
        verbose_name_plural = "Поля реквизитов"

    def __str__(self):
        return f'{self.title}: {self.value}'


class Details(models.Model):
    class Meta:
        verbose_name = "Реквизиты"
        verbose_name_plural = "Реквизиты"

    def __str__(self):
        return 'Реквизиты'
