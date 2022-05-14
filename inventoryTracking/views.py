from django.shortcuts import render
from .models import Item
# from .forms import ItemForm


def index(request):
    context = {'items': Item.objects.all()}
    return render(request, 'home.html', context=context)
