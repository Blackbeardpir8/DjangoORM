from core.models import Restaurant, Rating,Sale,Staff
from django.utils import timezone
from django.db.models.functions import Lower
def run():
    staff , created = Staff.objects.get_or_create(name = "John Wick")
    staff.restaurants.set(Restaurant.objects.all()[:10])
    italian = staff.restaurants.filter(restaurant_type = Restaurant.TypeChoices.ITALIAN)
    print(italian)
    



