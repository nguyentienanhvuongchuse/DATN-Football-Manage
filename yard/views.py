from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import *
from home.models import *
from .models import *
# Create your views here.

def booking(request):
    current_user = request.user.id
    location = Location.objects.get(user=current_user)

    booking = Booking.objects.raw(
        "SELECT yard_time.id"
        "from yard_yard join yard_time on yard_yard.id = yard_time.yard_id join home_booking on yard_time.id = home_booking.time_id"
        "where yard_yard.location_id=2"
    )

    context = {"booking":booking}
    return render(request, "manage/booking.html",context)

def manage_location(request):
    current_user = request.user.id
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
    current_user = request.user.id
    location_id = Location.objects.get(user=current_user)
    yard = Yard.objects.filter(location=location_id)
    context = {"yard":yard}
    return render(request, "manage/yard.html", context)

def update_yard(request,pk):
    yard = Yard.objects.get(id=pk)
    if request.method == "POST":
        form = YardForm(request.POST, instance=yard)
        if form.is_valid():
            form.save()
            return redirect("manage_yard")
    else:
        form = YardForm(instance=yard)
    context = {"form":form, "yard":yard}
    return render(request, "manage/form_yard.html", context)

def delete_yard(request,pk):
    yard = Yard.objects.get(id=pk)
    if request.method == "POST":
        yard.delete()
        return redirect("manage_yard")
    context = {"yard":yard}
    return render(request, "manage/delete_yard.html", context)

def create_yard(request):
    current_user = request.user.id
    location = Location.objects.get(user=current_user)
    form = CreateYardForm(initial={"location":location})
    if request.method == "POST":
        form = CreateYardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_yard")
    else:
        form = CreateYardForm(initial={"location":location})
    context = {"form":form}
    return render(request, "manage/create_yard.html", context)

def time_cost(request,pk):
    TimeFormSet = inlineformset_factory(Yard, Time,fields=("time","cost"),extra=5)
    yard = Yard.objects.get(id=pk)
    time = Time.objects.filter(yard=pk)

    formset = TimeFormSet(queryset=Time.objects.none(), instance=yard)
    if request.method == "POST":
        form = TimeCostForm(request.POST)
        formset = TimeFormSet(request.POST, instance=yard)
        if formset.is_valid():
            formset.save()
            return redirect("manage_yard")
    context = {"time":time, "form":formset}
    return render(request, "manage/time.html",context)

def update_timecost(request,pk):
    time = Time.objects.get(id=pk)
    yard = time.yard_id
    form = TimeCostForm(instance=time)
    if request.method == "POST":
        form = TimeCostForm(request.POST, instance=time)
        if form.is_valid():
            form.save()
            return redirect("create_time", pk=yard)
    context = {"form":form, "time":time}
    return render(request, "manage/update_time.html", context)

def update_timecost(request,pk):
    time = Time.objects.get(id=pk)
    yard = time.yard_id
    if request.method == "POST":
        time.delete()
        return redirect("create_time", pk=yard)
    context = {"time":time}
    return render(request, "manage/delete_time.html", context)

def statistical(request):
    return HttpResponse("Statistical")
