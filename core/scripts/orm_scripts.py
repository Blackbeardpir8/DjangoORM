from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    restraunts = Restaurant.objects.order_by('name')
    print(restraunts)
    
    
    



