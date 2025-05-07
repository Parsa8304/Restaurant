from django.urls import path
from . import views



urlpatterns = [
       path('register/', views.register, name='register'),
       path('registervendor/', views.register_vendor, name='register_vendor'),
]