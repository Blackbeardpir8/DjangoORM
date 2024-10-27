from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    restaurant = Restaurant.objects.first()
    print(restaurant.delete())
    



