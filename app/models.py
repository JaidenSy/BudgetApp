from django.contrib.auth.models import User
from django.db import models

class ItemType(models.Model):
    name = models.CharField(max_length=50)
    allocated_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    items = models.ManyToManyField(Item, through='BudgetItem')

    def __str__(self):
        return f"{self.user}'s Budget"

class BudgetItem(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.budget.user}'s {self.item.name} Budget Item"
