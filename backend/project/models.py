from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from core.models.components import Document


class ProjectStage(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В прогрессе'),
        ('suspended', 'Приостановлен'),
        ('completed', 'Завершён'),
    ]
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField(verbose_name='Номер этапа', blank=True, null=True, editable=False)
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    created_at = models.DateField(auto_now_add=True)
    progress = models.CharField(max_length=50, default='0%')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='stages')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус')

    def save(self, *args, **kwargs):
        if not self.order:
            max_number = ProjectStage.objects.filter(project=self.project).aggregate(models.Max('order'))[
                'order__max']
            self.order = max_number + 1 if max_number is not None else 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Этап проекта"
        verbose_name_plural = "Этапы проекта"

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stage = models.ForeignKey(ProjectStage, on_delete=models.CASCADE, related_name='tasks')
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title


class ProjectStageProgress(models.Model):
    stage = models.OneToOneField(ProjectStage, on_delete=models.CASCADE, related_name='progress_instance')
    total_tasks = models.IntegerField()
    completed_tasks = models.IntegerField(default=0)

    @property
    def completion_percentage(self):
        if self.total_tasks == 0:
            return 0
        return (self.completed_tasks / self.total_tasks) * 100


class Project(models.Model):
    STATUS_CHOICES = [
        ('init', 'Инициализация'),
        ('in_progress', 'В прогрессе'),
        ('suspended', 'Приостановлен'),
        ('completed', 'Завершён'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название')
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Заказчик')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectDocument(Document):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ проекта'
        verbose_name_plural = 'Документы проекта'