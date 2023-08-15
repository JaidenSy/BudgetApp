from django.contrib import admin
from .models import ItemType, Item, Budget, BudgetItem

admin.site.register(ItemType)
admin.site.register(Item)
admin.site.register(Budget)
admin.site.register(BudgetItem)
