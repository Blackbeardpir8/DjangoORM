from django.contrib import admin
from core.models import Restaurant,Sale,Rating
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Rating)
admin.site.register(Sale)