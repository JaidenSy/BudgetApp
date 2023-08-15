from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Item, UserIncome, UserCategoryBudget
from .serializers import CategorySerializer, ItemSerializer, UserIncomeSerializer, UserCategoryBudgetSerializer

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ItemCreateView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'message': 'Item created successfully'})
        return Response(serializer.errors, status=400)

class ItemListView(APIView):
    def get(self, request):
        Items = Item.objects.filter(user=request.user)
        serializer = ItemSerializer(Items, many=True)
        return Response(serializer.data)

class ItemDetailView(APIView):
    def get(self, request, Item_id):
        Item = get_object_or_404(Item, pk=Item_id, user=request.user)
        serializer = ItemSerializer(Item)
        return Response(serializer.data)

    def put(self, request, Item_id):
        Item = get_object_or_404(Item, pk=Item_id, user=request.user)
        serializer = ItemSerializer(Item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Item updated successfully'})
        return Response(serializer.errors, status=400)

    def delete(self, request, Item_id):
        Item = get_object_or_404(Item, pk=Item_id, user=request.user)
        Item.delete()
        return Response({'message': 'Item deleted successfully'})

class UserIncomeView(APIView):
    def post(self, request):
        serializer = UserIncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class UserBudgetView(APIView):
    def post(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        user = request.user
        serializer = UserCategoryBudgetSerializer(data=request.data)
        if serializer.is_valid():
            budget_amount = serializer.validated_data['budget_amount']
            user_budget, created = UserCategoryBudget.objects.get_or_create(user=user, category=category)
            user_budget.budget_amount = budget_amount
            user_budget.save()
            return Response({'message': 'Budget set successfully'})
        return Response(serializer.errors, status=400)
