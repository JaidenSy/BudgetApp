from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserIncome(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    income_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Income for {self.user.username}"

class UserCategoryBudget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Budget for {self.user.username} - {self.category.name}"
