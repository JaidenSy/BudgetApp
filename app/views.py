from django.shortcuts import render, redirect
from django.db.models import Sum, Q, F
from django.contrib.auth.decorators import login_required
from .models import Budget, ItemType, BudgetItem
from .forms import ItemTypeBudgetForm


@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    item_type_spending = (
        ItemType.objects
        .annotate(total_spent=Sum('item__budgetitem__allocated_amount'))
        .annotate(remaining_budget=F('allocated_budget') - F('total_spent'))
        .values('name', 'total_spent', 'remaining_budget')
    )
    return render(request, 'budget_list.html', {'budgets': budgets, 'item_type_spending': item_type_spending})

def budget_detail(request, budget_id):
    budget = Budget.objects.get(pk=budget_id)
    item_type_spending = (
        ItemType.objects
        .annotate(total_spent=Sum('item__budgetitem__allocated_amount', filter=Q(item__budgetitem__budget=budget)))
        .values('name', 'total_spent')
    )
    return render(request, 'budget_detail.html', {'budget': budget, 'item_type_spending': item_type_spending})

def update_allocated_budget(request, item_type_id):
    item_type = ItemType.objects.get(pk=item_type_id)

    if request.method == 'POST':
        form = ItemTypeBudgetForm(request.POST, instance=item_type)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = ItemTypeBudgetForm(instance=item_type)

    return render(request, 'update_allocated_budget.html', {'form': form, 'item_type': item_type})