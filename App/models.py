from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=12)

# Items (Bought items)
class Item(models.Model):
    name = models.CharField(max_length=12)
    price = models.DecimalField()
    category = models.ForeignKey(Category, related_name="item_category", on_delete=models.CASCADE)

# Budget (based on time)
class Budget(models.Model):
    name = models.CharField(max_length=12)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
