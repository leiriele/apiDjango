from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_nickname', 'user_name', 'user_email', 'user_age']
        
"""
class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model: UserTasks
        fields: 'user_nickname' 'user_task'
""" 