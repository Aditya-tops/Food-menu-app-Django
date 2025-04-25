from django.shortcuts import render,HttpResponse
from .models import Item
# Create your views here.

def index(request):
    return HttpResponse("Heloo World")

def item(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)

