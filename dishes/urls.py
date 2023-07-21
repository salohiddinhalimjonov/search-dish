from django.urls import path
from .views import search_dish, dish_restaurant

urlpatterns = [
    path('', search_dish, name='search_dish'),
    path('restaurants/<int:pk>', dish_restaurant, name="dish_restaurant")
]