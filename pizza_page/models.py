from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
import secrets


def save_img(instance, filename):
    random_hex = secrets.token_hex(8)
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (random_hex, ext)
    return os.path.join('food', filename)


class Food(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to=save_img, null=True)

    def __str__(self):
        return f"{self.name}"

class Price(models.Model):
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="price_food_id")
    name_selection = (
        ('M', 'Medium'),
        ('S', 'Small'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=1, choices=name_selection)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.get_name_display()}: {self.price}"

class Order(models.Model):
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_id")
    status_selection = (
        ('NP', 'Not Placed'),
        ('PL', 'Placed'),
        ('IN', 'In Progress'),
        ('CO', 'Completed'),
    )
    status = models.CharField(max_length=2, choices=status_selection)

    def __str__(self):
        return f"order no: {self.id}"


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_id")
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="order_food_id")
    food_price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name="order_price_id")
