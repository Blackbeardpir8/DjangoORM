from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    restaurants = Restaurant.objects.filter(name__gt = "E")
    print(restaurants)
    
    



