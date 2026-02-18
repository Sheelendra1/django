from django.urls import path
from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
    path('update/<int:id>/', update_stock, name='update_stock'),
]
