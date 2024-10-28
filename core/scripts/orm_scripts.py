from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    chinese = Restaurant.TypeChoices.CHINESE
    restaurants = Restaurant.objects.filter(restaurant_type=chinese,name__startswith='C')
    print(restaurants)

    
    



