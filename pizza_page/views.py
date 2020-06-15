from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Food, Price, OrderItem, Order

# Create your views here.
def main_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    elif request.method == "POST":

        # if request to add item to cart
        if 'food' and 'size' in request.POST:
            try:
                request.POST["food"]
                request.POST["size"]
            except:
                raise Http404("You Didn't Have a Correct Food Items In Your Cart")

            # load posted data into variables
            selectedfood = request.POST["food"]
            selectedsize = int(request.POST["size"])

            # get instances of database tables
            user_instance = User.objects.filter(username=request.user).first()
            food_instance = Food.objects.filter(name=selectedfood).first()
            price_instance = Food.objects.filter(name=selectedfood).first().price_food_id.all()[selectedsize]


            # if user already had a not placed order(cart), place next item in cart
            if not Order.objects.filter(cust_id=user_instance, status="NP"):
                order = Order(cust_id=request.user, status="NP")
                order.save()

            # continue: get instances of database tables
            order_instance = Order.objects.filter(cust_id=user_instance, status="NP").first()

            # save order items

            orderitem = OrderItem(order_id=order_instance, food_id=food_instance, food_price=price_instance)
            orderitem.save()

            return redirect("main_view")

        # if request to place an order
        else:
            if Order.objects.filter(cust_id=request.user, status='NP').first():
                order = Order.objects.filter(cust_id=request.user, status='NP').first()
            else:
                message = {"message": "you dont have food items in your cart yet", "category": "danger"}
                raise Http404("You Didn't Have Food Items In Your Cart")
            order.status = 'PL'
            order.save()

    # if get request
    context = {
        "user": request.user,
        "foods": Food.objects.all(),
        "prices": Price.objects.all(),
    }
    # check if user has (not placed) order and return items his cart
    try:
        context["fooditems"] = Order.objects.filter(cust_id=request.user.id, status="NP").first().order_id.all()
        context["total"] = 0
        for i in context["fooditems"]:
            context["total"] += i.food_price.price

    except AttributeError:
        pass

    # check if user has (placed) orders and return orders
    try:
        context["posted_orders"] = Order.objects.filter(cust_id=request.user.id).exclude(status="NP").all()

    except:
        pass

    return render(request, "main_page.html", context)

@login_required
def order(request, orderid):
    #
    try:
        posted_order = Order.objects.filter(id=orderid, cust_id=request.user.id).exclude(status="NP").first()
    except:
        raise Http404("You don't have orders yet")

    context = {
    "posted_order": posted_order
    }

    # check if user has (placed) orders and return orders
    try:
        context["posted_orders"] = Order.objects.filter(cust_id=request.user.id).exclude(status="NP").all()
    except:
        pass

    try:
        context["fooditems"] = Order.objects.filter(cust_id=request.user.id, id=orderid).first().order_id.all()
    except:
        raise Http404("You don't have an order with this no")

    context["total"] = 0

    for i in context["fooditems"]:
        context["total"] += i.food_price.price
    return render(request, "order.html", context)

@login_required
def orders_list(request):

    context = {}

    # check if user has (placed) orders and return orders
    try:
        context["posted_orders"] = Order.objects.filter(cust_id=request.user.id).exclude(status="NP").all()
    except:
        pass
    return render(request, "order_history.html", context)

def order_confirmation(request):
    return render(request, "place_order.html")

