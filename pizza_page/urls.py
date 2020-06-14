from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("<int:orderid>/", views.orders_list, name="orders_list"),
]