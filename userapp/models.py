from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default= 'default.jpg', upload_to='profile_pictures/', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

