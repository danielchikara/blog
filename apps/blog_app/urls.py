from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'blog'
urlpatterns = [
    # LOGIN
    path('create/', PostCreateView.as_view(), name='post_create'),


]