from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    print(Restaurant.objects.filter(restaurant_type= Restaurant.TypeChoices.CHINESE))
    



