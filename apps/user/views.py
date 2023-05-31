from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from apps.user.serializers import UserSerializer
from apps.user.models import *

# Create your views here.


class UserCreate(CreateAPIView):
    serializer_class = UserSerializer


class UserUpdate(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User


class UserDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User


class UserDelete(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User
