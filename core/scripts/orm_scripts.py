from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    chinese = Restaurant.TypeChoices.CHINESE
    indian = Restaurant.TypeChoices.INDIAN
    mexican = Restaurant.TypeChoices.MEXICAN
    check_types = [chinese,indian,mexican]
    restaurants = Restaurant.objects.filter(restaurant_type__in=check_types)
    print(restaurants)
    
    



