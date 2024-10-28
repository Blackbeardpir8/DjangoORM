from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    restaurant = Restaurant.objects.filter(name = "Pizzeria 1")
    print(restaurant)
    print(restaurant.get())
    



