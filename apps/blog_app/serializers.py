from rest_framework import serializers
from apps.blog_app.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = [ 'title', 'content', 'publication_date', 'category', 'tags']

        
