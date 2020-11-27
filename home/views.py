from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home page")

def detail(request):
    return HttpResponse("Detail page")

def contact(request):
    return HttpResponse("Contact page")

def login(request):
    return HttpResponse("Login page")

def signup(request):
    return HttpResponse("Signup page")
