from django.contrib import admin
from .models import Food,Price,Order,OrderItem

# Register your models here.
admin.site.register(Food)
admin.site.register(Price)
admin.site.register(Order)
admin.site.register(OrderItem)