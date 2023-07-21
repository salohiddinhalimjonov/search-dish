from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


# Create your views here.

def search_dish(request):
    dishes = None
    context = {'dishes': dishes}
    search = request.GET.get('search')
    if search:
        dishes = Item.objects.filter(name__icontains=search)

    if dishes:
        context['dishes'] = dishes
    return render(request, 'dishes.html', context)


def dish_restaurant(request, pk):
    restaurants = None
    context = {'restaurants': restaurants}
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        pass
    if item:
        result = RestaurantItem.objects.filter(item=item)
        context['restaurants'] = result
        context['item'] = item
    return render(request, 'restaurants.html', context)


