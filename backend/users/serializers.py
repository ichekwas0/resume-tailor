from rest_framework import serializers
from .models import MyUser

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'resume']
        
class RetrieveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'resume']