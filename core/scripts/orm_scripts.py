from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    Rating.objects.create(user = user, restaurant=restaurant , rating = 9)


