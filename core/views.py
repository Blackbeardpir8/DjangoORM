from django.shortcuts import render
from core.forms import RestaurantForm
from core.models import Restaurant,Sale,Rating
# Create your views here.

def index(request):
    restaurants = Restaurant.objects.prefetch_related('ratings','sales')
    context = {'restaurants': restaurants}
    return render(request, 'index.html',context)    