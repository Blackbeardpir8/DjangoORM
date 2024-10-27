from core.models import Restaurant, Rating, User
from django.utils import timezone

def run():
    Restaurant.objects.all().delete()
    



