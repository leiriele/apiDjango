from typing import __all__
from rest_framework import serializers
from .models import User, UserTasks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields: '__all__' # os dados que deseja retornar ao front
        
"""
class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model: UserTasks
        fields: 'user_nickname' 'user_task'
""" 