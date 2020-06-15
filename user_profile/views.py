from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def register_view(request):
        # check if user is already authenticated
        if request.user.is_authenticated:
                return redirect('main_view')

        # user is not authenticated, POST REQUEST
        elif request.method == "POST":
                print(request.POST)
                form = RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        messages.success(request, f"{username} you have registered successfully, "
                                                  f"now please login your account")
                        return redirect('login')
        # user is not authenticated, GET REQUEST
        else:
                form = RegisterForm()
        # return html page with either form
        return render(request, "register.html", {'form': form})
