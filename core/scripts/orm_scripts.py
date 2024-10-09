from core.models import Restaurant
from django.utils import timezone

def run():

    restaurant = Restaurant()
    restaurant.name = "THE ITALIAN PASTA"
    restaurant.website = "theitalianpasta@gmail.com"
    restaurant.latitude = 55.34
    restaurant.longitude = 87.23
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.Typechoices.ITALIAN

    restaurant.save()

