from rest_framework import serializers
from .models import *


class ProjectDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDocument
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    documents = ProjectDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class ProjectStageSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectStage
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    stages = ProjectStageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
