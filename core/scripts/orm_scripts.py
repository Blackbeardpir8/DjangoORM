from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    restaurant = Restaurant.objects.first()
    user = User.objects.first()

    Rating.objects.create(user=user,restaurant = restaurant, rating = 3)

