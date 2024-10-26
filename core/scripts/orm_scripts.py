from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    restaurants = Restaurant.objects.filter(name__startswith = 'T')
    print(restaurants)

    print(restaurants.update(
        date_opened= timezone.now()-timezone.timedelta(days=365)

    ))
