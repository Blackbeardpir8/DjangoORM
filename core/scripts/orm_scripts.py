from core.models import Restaurant, Rating,Sale
from django.utils import timezone
from django.db.models.functions import Lower
def run():
    chinese = Restaurant.TypeChoices.CHINESE
    sales = Sale.objects.filter(restaurant__restaurant_type=chinese)
    print(sales)

    
    



