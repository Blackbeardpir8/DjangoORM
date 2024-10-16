from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator,MaxLengthValidator

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

    def __str__(self):
        return self.name
    

class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MinLengthValidator(1),MaxLengthValidator(5)]
    )

    def __str__(self):
        return f"Rating:{self.rating}"
    
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.SET_NULL,null=True)
    income = models.DecimalField(max_digits=8,decimal_places=2)
    datetime = models.DateTimeField()


