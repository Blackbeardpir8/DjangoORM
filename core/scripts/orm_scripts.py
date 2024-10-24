from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    restaurants = Restaurant.objects.all()
    restaurants.update(date_opened = timezone.now())
