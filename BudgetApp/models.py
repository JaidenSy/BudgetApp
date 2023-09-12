from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Model for Category (food / necessity / discretionary)
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Model for specific Items (Line Items)
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Model for Budget (based per month with year) that is specific to a User and lists items
class Budget(models.Model):
    month = models.CharField(max_length=12)  
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999),
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_month_display()} {self.year} Budget for {self.user.username}"