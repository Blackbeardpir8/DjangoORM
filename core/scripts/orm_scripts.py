from core.models import Restaurant
from django.utils import timezone

def run():
    restaurants = Restaurant.objects.all()
    print(restaurants)

