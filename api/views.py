from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_url = {

        "List": '/api-list',
        "Detail": '/api-detail/<str:pk>/',
        "Create":'/api-create/',
        "Update":'/api-update/<str:pk>',
        "Delete": '/api-delete/<str:pl>',

    }

    return Response(api_url)



@api_view(['GET'])
def apiDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serialize = TaskSerializer(tasks, many=False)

    return Response(serialize.data)


@api_view(['GET'])
def apiList(request):
    tasks = Task.objects.all()
    serialize = TaskSerializer(tasks, many=True)

    return Response(serialize.data)

@api_view(['POST'])
def apiCreate(request):
    serialize = TaskSerializer(data = request.data)

    if serialize.is_valid():
        serialize.save()

    return Response(serialize.data)


@api_view(['POST'])
def apiUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serialize = TaskSerializer(instance = tasks ,data = request.data)
    if serialize.is_valid():
        serialize.save()

    return Response(serialize.data)

@api_view(['DELETE'])
def apiDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()

    return Response('Successfully Deleted')