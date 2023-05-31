from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    # LOGIN
    
    path('create/', UserCreate.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('detail/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='user_detail'),

]