from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    rating=Rating(user = user, restaurant=restaurant , rating = 9)

    rating.full_clean()
    rating.save()

