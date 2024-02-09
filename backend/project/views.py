from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import ProjectStage, Task, ProjectDocument, Project
from .serializers import *


class ProjectListCreateView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '').upper()
        return Project.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query.lower()))


class ProjectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
