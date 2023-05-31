from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, status
from .serializers import *
from rest_framework.response import Response
from apps.blog_app.models import *
from apps.permission import *
# Create your views here.


class PostCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBlogger | IsAdmin]
    authentication_class = (TokenAuthentication)
    serializer_class = PostSerializer


class PostUpdateView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBlogger | IsAdmin]
    authentication_class = (TokenAuthentication)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetailView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBlogger | IsAdmin]
    authentication_class = (TokenAuthentication)
    serializer_class = PostSerializer
    queryset = Post.objects.all()