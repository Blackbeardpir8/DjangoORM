from core.models import Restaurant, Rating,Sale,Staff
from django.utils import timezone
from django.db.models.functions import Lower
def run():
    restaurants = Restaurant.objects.get(pk=10)
    print(restaurants.staff_set.all())



