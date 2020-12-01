from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .form import CreateUserForm
# Create your views here.

def home(request):
    return render(request, "base/home.html")

def order(request):
    return render(request, "base/order.html")

def detail(request):
    return render(request, "base/detail.html")

def contact(request):
    return HttpResponse("Contact page")

def signin(request):
    return HttpResponse("Login page")

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
