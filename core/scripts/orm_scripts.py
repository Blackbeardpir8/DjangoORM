from core.models import Restaurant, Rating,Sale
from django.utils import timezone
from django.db.models.functions import Lower
def run():
    restraunts = Restaurant.objects.latest()
    print(restraunts)

    
    



