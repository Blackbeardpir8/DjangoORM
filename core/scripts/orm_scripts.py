from core.models import Restaurant
from django.utils import timezone

def run():
    Restaurant.objects.create(
        name = "THE INDIAN IDLI",
        date_opened = timezone.now(),
        restaurant_type = Restaurant.Typechoices.INDIAN,
        website = "theindialidli@gmail.com",
        latitude = 34.23,
        longitude = 67.35,
    )
