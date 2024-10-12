from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    rating = Rating.objects.first()
    print(rating.restaurant)




