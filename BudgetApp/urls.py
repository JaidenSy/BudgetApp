from django.urls import path
from .views import CategoryListView, ItemListView, ItemDetailView, UserIncomeView, UserBudgetView

app_name = 'budgetapp'

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:category_id>/', ItemListView.as_view(), name='item_list'),
    path('item/<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
    path('set_income/', UserIncomeView.as_view(), name='set_user_income'),
    path('set_budget/<int:category_id>/', UserBudgetView.as_view(), name='set_user_budget'),
]
