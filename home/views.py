from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "base/home.html")

def order(request):
    return render(request, "base/order.html")

def detail(request):
    return render(request, "base/detail.html")

def contact(request):
    return HttpResponse("Contact page")

def login(request):
    return HttpResponse("Login page")

def signup(request):
    return HttpResponse("Signup page")
