from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_picture/', default='defaultimage.jpg')
    location = models.CharField(max_length=100) # PIP INSTALL PILLOW for pic

    def __str__(self):
        return self.user.username
    

    



