from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Item
from .forms import ItemForm, ItemTempDeleteForm


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


# ================================
# E D I T  P A G E
# ================================

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            item.save()
        return redirect('index')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_edit.html', {'form': form})


# ================================
# T E M P  D E L E T E  P A G E
# ================================

def item_temp_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemTempDeleteForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
            item.is_deleted = True
            item.save(update_fields=['is_deleted'])
        return redirect('index')
    else:
        form = ItemTempDeleteForm(instance=item)
    return render(request, "item_temp_delete.html", {'form': form})


# ================================
# R E S T O R E  P A G E
# ================================

def item_restore(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.is_deleted = False
        item.save(update_fields=['is_deleted'])
        return redirect('index')
    return render(request, "item_restore.html", {'item': item})


# ================================
# T R A S H  B I N  P A G E
# ================================

def trash_bin(request):
    context = {'items': Item.objects.all()}
    return render(request, 'trash.html', context=context)


# ================================
# P E R M A  D E L E T E  P A G E
# ================================

def item_perma_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == "POST":
        item.delete()
        return HttpResponseRedirect("/")
    return render(request, "item_perma_delete.html")
