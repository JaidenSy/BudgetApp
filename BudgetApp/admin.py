from django.contrib import admin
from .models import Category, Item, UserCategoryBudget, UserIncome

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(UserCategoryBudget)
admin.site.register(UserIncome)
