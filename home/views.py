from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .form import CreateUserForm
from yard.models import *
# Create your views here.

def home(request):
    location = Location.objects.all()
    context = {"location": location}
    return render(request, "base/home.html", context)

def order(request):
    return render(request, "base/order.html")

def detail(request, pk):
    detail = Location.objects.get(id=pk)
    context = {"detail":detail}
    return render(request, "base/detail.html", context)

def contact(request):
    return HttpResponse("Contact page")

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("home")
    context = {}
    return render(request, "base/login.html", context)

def logout_user(request):
    logout(request)
    return redirect("home")

def signup(request):
    if request.method == "POST":
        form = CreateUserForm (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect("home")
    form = CreateUserForm()
    context = {"form":form}
    return render(request, "base/signup.html", context)
