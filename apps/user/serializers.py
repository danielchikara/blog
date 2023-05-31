from rest_framework import serializers
from apps.user.models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = User
        fields = '__all__'
        
    def get_image_url(self, obj):
        return obj.profile_image.url

