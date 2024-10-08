from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your modmels here.
class Restaurant(models.Model):
    class Typechoices(models.TextChoices):

        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'fast Food'
        OTHER = 'OT', 'Other'


    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2,choices=Typechoices.choices)

    def __init__(self):
        return self.name
    

class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating:{self.rating}"

