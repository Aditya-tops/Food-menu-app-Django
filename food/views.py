from django.shortcuts import render,HttpResponse,redirect
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# CRUD Operation
def index(request):
    item_list = Item.objects.all()
    return render(request,'food/index.html',{"item_list":item_list})

class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse('item_list')

def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    return render (request,'food/detail.html',{'item':item})

class FoodDetail(DetailView):
    model = Item;
    template_name = 'food/detail.html'
    


from .forms import ItemForm
def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})

def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'item':item,'form':form}) 

def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item}) 
    
# Authentication    
# signals     




