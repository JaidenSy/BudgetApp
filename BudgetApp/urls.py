from django.urls import path
from .views import CategoryListView, ItemListView, ItemDetailView, UserIncomeView, UserBudgetView

app_name = 'budgetapp'

urlpatterns = [
    path('api/categories/', CategoryListView.as_view(), name='category_list'),
    path('api/category/<int:category_id>/', ItemListView.as_view(), name='item_list'),
    path('api/item/<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
    path('api/set_income/', UserIncomeView.as_view(), name='set_user_income'),
    path('api/set_budget/<int:category_id>/', UserBudgetView.as_view(), name='set_user_budget'),
]
