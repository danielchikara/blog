from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self) -> str:
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    created_by = models.ForeignKey(
        User, related_name="post_created_by", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=500)
    publication_date = models.DateField(auto_now=True)
    category = models.ForeignKey(
        Category, related_name="posts_category", on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tags, related_name="tags_posts",  blank=True)

    def __str__(self) -> str:
        return self.title
