from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

