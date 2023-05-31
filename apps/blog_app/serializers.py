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
    tags = serializers.ListField(child=serializers.CharField(max_length=100), write_only=True)
    category = serializers.CharField(max_length=100)
    
    
    class Meta:
        model = Post
        fields = [ 'title', 'content', 'publication_date', 'category', 'tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        category_data = validated_data.pop('category')

        # Verificar si la categoría existe y obtenerla o crearla
        category, _ = Category.objects.get_or_create(name=category_data)

        # Verificar si las tags existen y obtenerlas o crearlas
        tags = []
        for tag_data in tags_data:
            tags_res, _ = Tags.objects.get_or_create(name=tag_data)
            tags.append(tags_res)

        user = self.context['request'].user
        print(user)
        post = Post.objects.create(category=category, created_by=user,  **validated_data)
        post.tags.set(tags)
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        category_data = validated_data.pop('category')

        # Verificar si la categoría existe y obtenerla o crearla
        category, _ = Category.objects.get_or_create(name=category_data)

        # Verificar si las etiquetas existen y obtenerlas o crearlas
        tags = []
        for tags_data in tags_data:
            tags_res, _ = Tags.objects.get_or_create(name=tags_data)
            tags.append(tags_res)

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.category = category
        instance.tags.set(tags)
        instance.save()
        return instance