from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LocationForm
from .models import *
# Create your views here.

def booking(request):
    return HttpResponse("Booking")

def manage_location(request):
    current_user = request.user.id
    print(current_user)
    location = Location.objects.get(user=current_user)

    form = LocationForm(instance=location)
    if request.method == "POST":
        form = LocationForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
            return redirect("manage_location")
    context = {"form":form}
    return render(request, "manage/location.html", context)

def manage_yard(request):
    return HttpResponse("Admin Yard")

def statistical(request):
    return HttpResponse("Statistical")
