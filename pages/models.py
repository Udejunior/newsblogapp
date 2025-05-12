from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    





# Create your models here.
class Blog_Post(models.Model):
    image = models.ImageField(upload_to = 'img', null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title 