from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    restaurant = Restaurant.objects.first()
    restaurant.name = "THE ITALIAN PIZZA PASTA AND RAAIOLI"
    restaurant.save()
