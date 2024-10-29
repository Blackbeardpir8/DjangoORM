from core.models import Restaurant, Rating,Sale
from django.utils import timezone
from django.db.models.functions import Lower
def run():
    restraunts = Restaurant.objects.order_by('date_opened')[:5]
    print(restraunts)

    
    



