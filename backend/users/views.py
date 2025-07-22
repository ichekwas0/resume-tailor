from django.shortcuts import render
from .serializers import CreateUserSerializer, RetrieveUserSerializer
from .models import MyUser
from rest_framework import generics

# Create your views here.
class CreateUserView(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = CreateUserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RetrieveUserSerializer
    lookup_field = 'id'

