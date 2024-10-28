from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    print(Restaurant.objects.count())
    print(Rating.objects.count())
    print(Sale.objects.count())
    



