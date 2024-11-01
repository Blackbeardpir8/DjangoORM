from django.shortcuts import render
from core.forms import RestaurantForm
from core.models import Restaurant,Sale,Rating
from django.db.models import Sum,Prefetch
from django.utils import timezone
# Create your views here.

def index(request):
    #Get all 5star rating and fetch all the sales for the restaurants with 5 stae ratings
    month_ago = timezone.now()-timezone.timedelta(days=30)
    monthly_sales = Prefetch(
        'sales',
        queryset=Sale.objects.filter(datetime__gte=month_ago)
    )
    restaurants = Restaurant.objects.filter(ratings__rating=5).prefetch_related('ratings', monthly_sales).annotate(total=Sum('sales__income'))
    restaurants.annotate(total=Sum('sales__income'))
    print([r.total for r in restaurants])
    return render(request, 'index.html')     