from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
# def index(request):
#     item_list= item.objects.all()
#     context= {
#         'item_list': item_list, 
#     }
#     return render(request,'food/index.html', context)

class IndexClassView(ListView):
    model= item;
    template_name='food/index.html'
    context_object_name='item_list'





def items(request):
    return HttpResponse('This is an item view')

def pause_video(request):
    return HttpResponse('YOU HAVE PAUSED THE VIDEO AND YOU ARE NOW PRACTICING DJANGO ON YOUR OWN!')


def detail(request,item_id):
    Item = item.objects.get(pk=item_id)
    context={
        'Item':Item,
    }

    return render(request,'food/detail.html',context)






def create_item(request):
    form= ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item_form.html',{'form':form})

def update_item(request,id):
    Item= item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=Item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item_form.html',{'form':form,'Item':Item})


def delete_item(request,id):
    Item=item.objects.get(id=id)
    if request.method=='POST':
        Item.delete()
        return redirect('food:index')
    return render (request,'food/item_delete.html',{'Item':Item})