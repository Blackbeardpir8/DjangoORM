from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    user = User.objects.first()
    restaurant = Restaurant.objects.first()

    print(Rating.objects.get_or_create(
        restaurant = restaurant,
        user = user,
        rating =4
    ))



