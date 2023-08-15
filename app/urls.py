from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_list, name='budget_list'),
    path('budget/<int:budget_id>/', views.budget_detail, name='budget_detail'),
    path('item_type/<int:item_type_id>/update_budget/', views.update_allocated_budget, name='update_allocated_budget'),
]