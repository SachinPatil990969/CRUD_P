from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemFrom
from .models import Item

# Create your views here.
def item_list_view(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items':items})

def add_item_view(request):
    if request.method == 'POST':
        form = ItemFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list_view')
    else:
        form = ItemFrom()

    return render(request, 'add_item.html', {'form':form})

def item_details_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_details.html', {'item':item})

def item_edit_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemFrom(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list_view')
        
    else:
        form = ItemFrom(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})

def item_delete_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('Item_list_view')