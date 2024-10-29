from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    chinese = Restaurant.TypeChoices.CHINESE
    indian = Restaurant.TypeChoices.INDIAN
    check_types = [chinese,indian]
    restaurants = Restaurant.objects.exclude(restaurant_type__in = check_types)
    print(restaurants)
    
    



