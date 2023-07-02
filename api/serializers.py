from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from projects.models import Project
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    class Meta:
        model = Project
        fields = '__all__'
