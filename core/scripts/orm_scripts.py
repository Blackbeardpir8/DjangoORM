from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    restaurant = Restaurant.objects.filter(restaurant_type = Restaurant.TypeChoices.ITALIAN)
    print(restaurant.exists())
    
    



