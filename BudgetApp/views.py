# views.py in your app
from django.shortcuts import render, redirect
from .models import Category, Item, Budget
from .forms import CategoryForm, BudgetForm, ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'budget/home.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('home')  # Redirect to the desired page after registration (change 'home' to your URL name)
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')  # Redirect to the desired page after login (change 'home' to your URL name)
        else:
            messages.error(request, 'Login failed. Please check your username and password.')

    return render(request, 'login.html')

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')  # Redirect to the category list view
    else:
        form = CategoryForm()
    return render(request, 'budget/create_category.html', {'form': form})

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')  # Redirect to the items list page after item creation
    else:
        form = ItemForm()

    return render(request, 'budget/create_item.html', {'form': form})
    
@login_required
def create_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user  # Assign the current user to the budget
            budget.save()
            return redirect('budgets')  # Redirect to the budget list view
    else:
        form = BudgetForm()
    return render(request, 'budget/create_budget.html', {'form': form})

@login_required
def category_list(request):
    categories = Category.objects.filter()
    return render(request, 'budget/category_list.html', {'categories': categories})

@login_required
def item_list(request):
    items = Item.objects.filter()  # Filter by user if necessary
    return render(request, 'budget/item_list.html', {'items': items})

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'budget/budget_list.html', {'budgets': budgets})