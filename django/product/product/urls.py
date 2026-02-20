from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import ProductViewSet # importing the file views.py from app folder
# or : from app import views

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet) # r'products' is the url endpoint (/products)
# or : router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # include the router urls
]