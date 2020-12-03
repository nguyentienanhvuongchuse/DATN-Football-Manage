from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def booking(request):
    return HttpResponse("Booking")

def manage_location(request):
    return HttpResponse("Admin Location")

def manage_yard(request):
    return HttpResponse("Admin Yard")

def statistical(request):
    return HttpResponse("Statistical")
