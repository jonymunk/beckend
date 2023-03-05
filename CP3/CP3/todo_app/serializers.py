from rest_framework import serializers
from todo_app.models import TodoList, Todo


class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(min_length=5, max_length=100, allow_null=False)

    def create(self, validated_data):
        TodoList = TodoList(**validated_data)
        TodoList.save()
        return TodoList

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(min_length=5, max_length=100, allow_null=False)
    TodoList = TodoListSerializer(required=False, read_only=True)
    TodoList_id = serializers.IntegerField(write_only=True)



    def create(self, validated_data):
        Todo = Todo(**validated_data)
        Todo.save()
        return Todo

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.TodoList_id = validated_data.get('TodoList_id', instance.TodoList_id)

        instance.save()
        return instance
