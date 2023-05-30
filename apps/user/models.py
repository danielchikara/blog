from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name= 'users_rol')
    biography = models.TextField(max_length=250)
    profile_image = models.ImageField(upload_to='profile_images/')
    
    def __str__(self) -> str:
        return self.username
    
    