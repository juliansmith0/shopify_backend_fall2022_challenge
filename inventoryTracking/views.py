from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


# ================================
# I N D E X / H O M E
# ================================

def index(request):
    context = {'items': Item.objects.all()}
    return render(request, 'home.html', context=context)


# ================================
# C R E A T I O N  P A G E 
# ================================

def item_creation(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            item.save()
        return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'item_new.html', {'form': form})
