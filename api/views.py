from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.request import Request
from .serializers import TaskSerializer
from .models import Task
from django.views import View
from django.contrib.auth.models import User

@api_view(['POST'])
def addTask(request:Request):
    data = request.data
    serializer = TaskSerializer(data=data)
  
    if serializer.is_valid():
        serializer.save()
        return Response({'result': 'Student added successfully'})
    else:
        return Response(serializer.errors)
    
@api_view(['GET'])
def getTask(request:Request, id):
    try:
        tasks=Task.objects.get(id=id)
        serializer=TaskSerializer(tasks)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response({'id':'is not task'})
    

@api_view(['GET'])
def getDelet(request:Request, id):
    tasks=Task.objects.get(id=id)
    tasks.delete()
    return Response({'id':'id is delet'})

@api_view(['POST'])
def Updatetask(request:Request, id):
    data=Task.objects.get(id==id)
    data=request.data
    data={
        'task':data.get('task'),
        'description':data.get('description'),
        'status':data.get('status')
    }
    serializer=TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
