from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from .models import Task
from todo.tasks import send_performend_mail

class TaskSerializers(serializers.Serializer):
    task_title = serializers.CharField(max_length=100)
    task_description = serializers.CharField()
    deadline = serializers.DateTimeField()
    performed = serializers.BooleanField(default=False)
    ID = serializers.IntegerField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instane, validated_data):
        instane.ID = validated_data.get('ID', instane.ID)
        instane.task_title = validated_data.get('task_title', instane.task_title)
        instane.task_description = validated_data.get('task_description', instane.task_description)
        instane.deadline = validated_data.get('deadline', instane.deadline)
        temp_performed = instane.performed
        instane.performed = validated_data.get('performed', instane.performed)
        if temp_performed != validated_data.get('performed', instane.performed):
            send_performend_mail.delay(instane.pk)
        
        instane.save()
        return instane
