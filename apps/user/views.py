from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from apps.user.serializers import UserSerializer
from apps.user.models import *
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class UserCreate(CreateAPIView):
    serializer_class = UserSerializer


class UserUpdate(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = (TokenAuthentication)
    
    def get_queryset(self):
        user = self.request.user
        if user.id ==  self.kwargs['pk'] or user.role.name == "Admin":
            return User.objects.filter(id=self.kwargs['pk'])
        return Response(status=status.HTTP_404_NOT_FOUND)
        

class UserDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    
    
    def get_queryset(self):
        user = self.request.user
        if user.id ==  self.kwargs['pk'] or user.role.name == "Admin":
            return User.objects.filter(id=self.kwargs['pk'])
        return Response(status=status.HTTP_404_NOT_FOUND)
        


class UserDelete(DestroyAPIView):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.id ==  self.kwargs['pk'] or user.role.name == "Admin":
            return User.objects.filter(id=self.kwargs['pk'])
        return Response(status=status.HTTP_404_NOT_FOUND)
