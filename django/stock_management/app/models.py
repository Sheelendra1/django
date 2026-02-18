from django.db import models
from django.core.exceptions import ValidationError

class Product(models.Model):

    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def clean(self):
        if self.quantity < 0:
            raise ValidationError("Stock cannot be negative")

    def __str__(self):
        return self.name
