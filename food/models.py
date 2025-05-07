from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # its user for getabsoluteuel for rediret page
# Create your models here.

class Item(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.shutterstock.com/shutterstock/photos/2059817444/display_1500/stock-vector-no-image-available-photo-coming-soon-illustration-vector-2059817444.jpg")
    
    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    

