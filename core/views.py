from django.shortcuts import render
from core.forms import RestaurantForm
from core.models import Restaurant,Sale,Rating,Staff
from django.db.models import Sum,Prefetch
from django.utils import timezone
# Create your views here.

def index(request):
    staff , created = Staff.objects.get_or_create(name = "John Wick")
    print(staff)
    print(type(staff.restaurants))
    print(staff.restaurants.all())