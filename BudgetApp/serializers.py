from rest_framework import serializers
from .models import Category, Item, UserIncome, UserCategoryBudget

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserIncome
        fields = '__all__'

class UserCategoryBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCategoryBudget
        fields = '__all__'
