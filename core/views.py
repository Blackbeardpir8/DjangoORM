from django.shortcuts import render
from core.forms import RestaurantForm
from core.models import Restaurant,Sale,Rating
# Create your views here.

def index(request):
    ratings = Rating.objects.select_related('restaurant')
    context = {'ratings':ratings}
    return render(request, 'index.html',context)    