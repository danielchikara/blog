from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class SocialUserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True,
                          is_superuser=True,  ** kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name='users_rol', null=True, blank=True)
    biography = models.TextField(max_length=250)
    profile_image = models.ImageField(upload_to='profile_images/')

    def __str__(self) -> str:
        return self.username
