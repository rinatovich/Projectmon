from django.urls import path
from .views import ProjectStageListCreateView, ProjectStageDetailView, TaskListCreateView, TaskDetailView, \
    ProjectDocumentListCreateView, ProjectDocumentDetailView, ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('project-stages/', ProjectStageListCreateView.as_view(), name='project-stage-list-create'),
    path('project-stages/<int:pk>/', ProjectStageDetailView.as_view(), name='project-stage-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('project-documents/', ProjectDocumentListCreateView.as_view(), name='project-document-list-create'),
    path('project-documents/<int:pk>/', ProjectDocumentDetailView.as_view(), name='project-document-detail'),
    path('project/', ProjectListCreateView.as_view(), name='project-list-detail'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]