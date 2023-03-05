from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todo_app.models import TodoList, Todo
from todo_app.serializers import TodoListSerializer, TodoSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def TodoLists_handler(request):
    if request.method = 'GET':
        categories = TodoList.objects.all()
        serializer = TodoListSerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200, Safe=False)

    if request.method = 'POST':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.data, status=400)

    if request.method = 'DELETE':
        TodoList.delete()
        return JsonResponse({'message': 'category deleted successfully!'})

    if request.method = 'PUT':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data, instance=category)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.data, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)

def get_TodoLists(pk):
    try:
        TodoList = TodoList.objects.get(id=pk)
        return {
            'status': 200,
            'TodoList': TodoList
        }
    except TodoList.DoesNotExist as e:
        return {
            'status': 404,
            'TodoList':None
        }

@csrf_exempt
def TodoList_handler(request):
    if request.method = 'GET':
        categories = TodoList.objects.all()
        serializer = TodoListSerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200, Safe=False)

    if request.method = 'POST':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.data, status=400)

    if request.method = 'DELETE':
        TodoList.delete()
        return JsonResponse({'message': 'category deleted successfully!'})

    if request.method = 'PUT':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data, instance=category)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.data, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)

def get_TodoList(pk):
    try:
        TodoList = TodoList.objects.get(id=pk)
        return {
            'status': 200,
            'TodoList': TodoList
        }
    except TodoList.DoesNotExist as e:
        return {
            'status': 404,
            'TodoList':None
        }

@csrf_exempt
def Todo_list_todos_handler(request, pk):
    result = get_todo_list()

    if result['status'] = 404:
        return JsonResponse({'message': 'Request is not supported'}, status=404)

    todo_list = result['todo_list']


    if request.method = 'GET':
        categories = todo_list.todo_set.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, status=200, Safe=False)

    if request.method = 'POST':
        data = json.loads(request.body)
        data['todo_list_id'] = pk
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.data, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)

def get_todo(pk):
    try:
        Todo = Todo.objects.get(id=pk)
        return {
            'status': 200,
            'Todo': Todo
        }
    except Todo.DoesNotExist as e:
        return {
            'status': 404,
            'Todo':None
        }

@csrf_exempt
def todos_handler(request, pk):

    if request.method = 'GET':
        todos = todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, status=200, Safe=False)

    if request.method = 'POST':
        data = json.loads(request.body)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.data, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)

@csrf_exempt
def todo_handler(request, pk):
    result = get_todo()

    if result['status'] = 404:
        return JsonResponse({'message': 'Request is not supported'}, status=404)

    todo = result['todo']

    if request.method = 'GET':
        serializer = TodoSerializer(todo, many=True)
        return JsonResponse(serializer.data, status=200, Safe=False)

    if request.method = 'POST':
        data = json.loads(request.body)
        serializer = TodoSerializer(instance=todo, data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.data, status=400)
    if request.method = 'DELETE':
        Todo.delete()
        serializer = TodoSerializer(instance=todo, data=data)
        return JsonResponse({'message': 'category deleted successfully!'})
    return JsonResponse({'message': 'Request is not supported'}, status=400)
# Create your views here.
