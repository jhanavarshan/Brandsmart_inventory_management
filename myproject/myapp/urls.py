from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('production/', views.production, name='production'),
    path('dovegel/', views.dovegel, name='dovegel'),
    path('inventory/', views.inventory, name='inventory'),
    path('products/', views.products, name='products'),
    path('stored_products/', views.stored_products, name='stored_products'), 
    path('rawmaterials/', views.rawmaterials, name='rawmaterials'),
     path('add_raw_materials/', views.add_raw_materials, name='add_raw_materials'),
]