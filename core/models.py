from typing import Any
from django.db import models

# Create your modmels here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __init__(self):
        return self.name