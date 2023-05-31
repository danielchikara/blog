from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, status
from .serializers import *
from rest_framework.response import Response
from apps.blog_app.models import *
from django.db import transaction
# Create your views here.


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        post_serializer = self.get_serializer(data=data)
        category_serializer = CategorySerializer(data=data.get('category'))
        tags_serializer = TagSerializer(data=data.get('tags'), many=True)

        with transaction.atomic():
            if post_serializer.is_valid() and category_serializer.is_valid() and tags_serializer.is_valid():
                category = category_serializer.save()
                tags = tags_serializer.save()
                post = post_serializer.save(category=category, created_by=request.user)
                post.tags.set(tags)
                return Response(post_serializer.data, status=status.HTTP_201_CREATED)

        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)