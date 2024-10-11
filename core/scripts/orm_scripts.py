from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    restaurant = Restaurant.objects.first()
    print(restaurant.name)

    #restaurant.name = "THE ITALIAN PIZZA NAD PASTA"
    #restaurant.save()


