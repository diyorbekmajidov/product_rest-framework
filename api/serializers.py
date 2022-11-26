from .models import Task
from rest_framework import serializers
from django.contrib.auth.models import User

class TaskSerializer(serializers.Serializer):
    task=serializers.CharField(max_length=255)
    description=serializers.CharField(max_length=255)
    status=serializers.BooleanField(default=False) 
    created_at=serializers.DateTimeField(read_only=True)
    updated_at=serializers.DateTimeField(read_only=True)
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data)  