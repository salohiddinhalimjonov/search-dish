import jsonfield
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Location(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Item(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Restaurant(BaseModel):
    name = models.CharField(max_length=128)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    full_details = jsonfield.JSONField(default={})
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class RestaurantItem(BaseModel):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name="restaurants")
    price = models.CharField(max_length=64)


__all__ = ["Location", "Item", "Restaurant", "RestaurantItem"]
