from django.contrib import admin
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from core.admin import DocumentAdmin
from project.models import *


class ProjectDocumentInline(admin.TabularInline):
    model = ProjectDocument
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'stage', 'completed')
    list_filter = ('stage__project',)
    search_fields = ('title', 'description')


@receiver([post_save, post_delete], sender=Task)
def update_stage_progress(sender, instance, **kwargs):
    stage = instance.stage
    if stage:
        completed_tasks_count = Task.objects.filter(stage=stage, completed=True).count()
        total_tasks_count = Task.objects.filter(stage=stage).count()
        if total_tasks_count > 0:
            stage.progress = f"{completed_tasks_count * 100 / total_tasks_count:.2f}%"
        else:
            stage.progress = "0%"
        stage.save()


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    inlines = [ProjectDocumentInline]


@receiver(pre_save, sender=ProjectStage)
def set_order(sender, instance, **kwargs):
    if instance.order is None:
        max_order = ProjectStage.objects.filter(project=instance.project).aggregate(models.Max('order'))['order__max']
        instance.order = 1 if max_order is None else max_order + 1


@admin.register(ProjectStage)
class ProjectStageAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display = (
        'title', 'order', 'start_date', 'end_date', 'progress', 'status', 'project')
    readonly_fields = ('order', 'progress',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'stage', 'completed')
    list_filter = ('stage__project', 'completed')
    search_fields = ('title', 'description')
    inlines = [ProjectDocumentInline]


class ProjectStageInline(admin.TabularInline):
    model = ProjectStage
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'start_date')
    search_fields = ('title',)
    inlines = [ProjectStageInline]


@admin.register(ProjectDocument)
class ProjectDocumentAdmin(DocumentAdmin):
    list_display = ['file', 'task']
