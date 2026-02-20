from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price=models.FloatField()
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    address=models.TextField()
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} X {self.product.name} in Order {self.order.id}"