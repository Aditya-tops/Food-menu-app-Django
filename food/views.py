from django.shortcuts import render,HttpResponse
from .models import Item
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list":item_list,
    }
    return render(request,'food/index.html',context)

def item(request):
    return HttpResponse('item_list')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render (request,'food/detail.html',context)