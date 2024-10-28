from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    chinese = Restaurant.TypeChoices.CHINESE
    restaurants = Restaurant.objects.exclude(restaurant_type=chinese)
    print(restaurants)
    
    



