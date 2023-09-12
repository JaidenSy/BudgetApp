from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration_view, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create-category/', views.create_category, name='create_category'),
    path('create-budget/', views.create_budget, name='create_budget'),
    path('categories/', views.category_list, name='categories'),
    path('items/create/', views.create_item, name='create_item'),
    path('items/', views.item_list, name='items'),
    path('budgets/', views.budget_list, name='budgets'),
]
