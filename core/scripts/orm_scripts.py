from core.models import Restaurant, Rating,Sale
from django.utils import timezone

def run():
    sales = Sale.objects.filter(income__range = (50,60))
    print(sales)
    
    



