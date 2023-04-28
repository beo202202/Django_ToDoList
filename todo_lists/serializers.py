from rest_framework import serializers
from todo_lists.models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'id': {'read_only': True}
        }

class TodoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ("title",)
        read_only_fields = ('id',)
        extra_kwargs = {
            'id': {'read_only': True}
        }
        
