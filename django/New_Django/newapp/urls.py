from django.urls import path
from . import views

urlpatterns = [
    path('student/<str:name>/', views.student_view, name='student'),
]