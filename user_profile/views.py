from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm


def register_view(request):
        form = RegisterForm()
        return render(request, "register.html", {'form': form})
