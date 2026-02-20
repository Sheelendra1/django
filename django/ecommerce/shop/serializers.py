from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Order, Category, Profile, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['__all__']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['__all__']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['__all__']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['__all__']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['__all__']
