from core.models import Restaurant, Rating,Sale,Staff
from django.utils import timezone
from django.db.models.functions import Lower
def run():
    staff , created = Staff.objects.get_or_create(name = "John Wick")
    print(staff.restaurants.all())
    staff.restaurants.add(Restaurant.objects.first())
    print(staff.restaurants.all())
    



