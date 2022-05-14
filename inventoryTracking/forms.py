from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity']

class ItemTempDeleteForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['deletion_comment']
