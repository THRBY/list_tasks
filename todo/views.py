from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.core.mail import send_mail

from .models import Task
from .serializers import TaskSerializers

# Create your views here.
class TaskView(APIView):
    def get(self, request, pk=None):
        if pk == None:            
            tasks = Task.objects.all()
            serializer = TaskSerializers(tasks, many=True)
            return Response({
                "Задачи": serializer.data
                })
        elif pk!=None:
            tasks = get_object_or_404(Task.objects.all(), pk=pk)
            serializer = TaskSerializers(tasks)
            return Response({
                "Задача": serializer.data
                })

    def post(self, request, pk=None, execute=None):
        if pk==None and execute==None:
            task = request.data.get('task')
            # Create new task 
            serializer = TaskSerializers(data=task)
            if serializer.is_valid(raise_exception=True):
                task_saved = serializer.save()
            return Response({
                "success": "Задача '{}' создана успешно".format(task_saved.task_title)
                })
        else:
            return Response({
                "Пусто"
            })

    def patch(self, request, pk):
        saved_task = get_object_or_404(Task.objects.all(), pk=pk)
        data = request.data.get('task')
        serializer = TaskSerializers(instance=saved_task, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            saved_task = serializer.save()
        return Response({
            "success": "Задача '{}' успешно изменина".format(saved_task.task_title)
            })

    def delete(self, request, pk):
         task = get_object_or_404(Task.objects.all(), pk=pk)
         task.delete()
         return Response({
             "alarm": "Задача с id '{}' была удалена".format(pk)
         }, status=204)
