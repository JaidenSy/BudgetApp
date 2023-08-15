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

class ItemListView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        items = Item.objects.filter(category=category)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class ItemDetailView(APIView):
    def get(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def post(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, item_id):
        item = get_object_or_404(Item, pk=item_id)
        item.delete()
        return Response(status=204)

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
        serializer = UserCategoryBudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
