from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from employees.models import Employee
from empoyees.serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def Employee_handler(request):
    if request.method = 'GET':
        categories = Employee.objects.all()
        serializer = EmployeeSerializer(categories, many=True)
        return JsonResponse(serializer.data, status=200, Safe=False)

    if request.method = 'POST':
        data = json.loads(request.body)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.data, status=400)

    if request.method = 'DELETE':
        employee.delete()
        return JsonResponse({'message': 'category deleted successfully!'})

    if request.method = 'PUT':
        data = json.loads(request.body)
        serializer = EmployeeSerializer(data=data, instance=category)
        if serializer.is_valid():
           serializer.save()
           return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.data, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)

def get_Employee(pk):
    try:
        employee = Employee.objects.get(id=pk)
        return {
            'status': 200,
            'employee': employee
        }
    except Employee.DoesNotExist as e:
        return {
            'status': 404,
            'employee':None
        }

# Create your views here.
