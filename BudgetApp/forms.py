# forms.py in your app
from django import forms
from .models import Category, Budget, Item

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['month', 'year', 'limit']

    def __init__(self, user, *args, **kwargs):
        super(BudgetForm, self).__init__(*args, **kwargs)
        self.fields['month'].widget.attrs.update({'class': 'form-control'})  # Add CSS class for styling
        self.fields['year'].widget.attrs.update({'class': 'form-control'})   # Add CSS class for styling
        self.fields['limit'].widget.attrs.update({'class': 'form-control'})  # Add CSS class for styling
        self.fields['user'].initial = user  # Set the user field to the current user
        self.fields['user'].widget = forms.HiddenInput()  # Hide the user field from the form

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'category']