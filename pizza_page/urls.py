from django.urls import path
from . import views

urlpatterns = [
    path("/", views.main_view, name="main_view"),
    path("<int:orderid>/", views.order, name="order"),
    path("orders/", views.orders_list, name="orders_list"),
    path("order_placement/", views.order_confirmation, name="order_confirmation"),
]