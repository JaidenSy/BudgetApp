from django import forms
from .models import ItemType

class ItemTypeBudgetForm(forms.ModelForm):
    class Meta:
        model = ItemType
        fields = ['allocated_budget']