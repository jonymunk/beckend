from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(min_length=5, max_length=100, allow_null=False)
    position = serializers.CharField(min_length=5, max_length=100, allow_null=False)
    salary = serializers.Integerfield(write_only=True)

    def create(self, validated_data):
        Employee = Employee(**validated_data)
        Employee.save()
        return Employee

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get('name', instance.full_name)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.position = validated_data.get('position', instance.position)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.salary = validated_data.get('name', instance.salary)
        instance.save()
        return instance
