from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from django.views import View
from .models import Category, Item, UserIncome, UserCategoryBudget

class CategoryListView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'category_list.html', {'categories': categories})

class ItemListView(View):
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        items = Item.objects.filter(category=category)
        return render(request, 'item_list.html', {'category': category, 'items': items})

class ItemDetailView(View):
    def get(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        return render(request, 'item_detail.html', {'item': item})

    def post(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.save()
        return redirect('item_detail', item_id=item_id)

    def delete(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        return redirect('category_list')

class UserIncomeView(View):
    def post(self, request):
        income_amount = request.POST['income_amount']
        user_income, created = UserIncome.objects.get_or_create(user=request.user)
        user_income.income_amount = income_amount
        user_income.save()
        return redirect('category_list')

class UserBudgetView(View):
    def post(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        budget_amount = request.POST['budget_amount']
        user_budget, created = UserCategoryBudget.objects.get_or_create(user=request.user, category=category)
        user_budget.budget_amount = budget_amount
        user_budget.save()
        return redirect('category_list')
