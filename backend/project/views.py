from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import ProjectStage, Task, ProjectDocument, Project
from .serializers import ProjectStageSerializer, TaskSerializer, ProjectDocumentSerializer, ProjectSerializer


class ProjectStageListCreateView(generics.ListCreateAPIView):
    queryset = ProjectStage.objects.all()
    serializer_class = ProjectStageSerializer


class ProjectStageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectStage.objects.all()
    serializer_class = ProjectStageSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectDocumentListCreateView(generics.ListCreateAPIView):
    queryset = ProjectDocument.objects.all()
    serializer_class = ProjectDocumentSerializer


class ProjectDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectDocument.objects.all()
    serializer_class = ProjectDocumentSerializer


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
