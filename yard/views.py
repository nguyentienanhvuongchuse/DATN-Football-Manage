from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date,datetime
from django.core import serializers
from home.decorators import *
from .forms import *
from home.models import *
from .models import *
import json
# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def booking(request):
    current_user = request.user.id
    location = Location.objects.get(user=current_user)
    booking = ViewBooking.objects.filter(location=location, status="XL")
    if request.method == "POST":
        booking_id = request.POST["booking_id"]
        data = Booking.objects.get(id=booking_id)
        data.status = request.POST["handle"]
        data.save()
    context = {"booking":booking}
    return render(request, "manage/booking.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def booking_open(request):
    current_user = request.user
    location = Location.objects.get(user=current_user)
    yard = Yard.objects.filter(location=location)
    booking = BookingView.objects.filter(location=location, status="M")
    if request.method == "POST":
        time = request.POST["drop"]
        date = request.POST["date"]
        book = Booking.objects.create(time_id=time,user=current_user,date=date)
        book.save()
    context = {"booking":booking, "yard":yard}
    return render(request, "manage/booking_open.html",context)

def timeAjax(request,pk):
    time = Time.objects.filter(yard=pk)
    responseData = serializers.serialize('json',time)
    return JsonResponse(responseData, safe=False)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def booking_close(request):
    current_user = request.user.id
    location = Location.objects.get(user=current_user)
    booking = BookingView.objects.filter(location=location, status="TC")
    context = {"booking":booking}
    return render(request, "manage/booking_close.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def booking_accept(request):
    current_user = request.user.id
    location = Location.objects.get(user=current_user)
    booking = ViewBooking.objects.filter(location=location, status="XN")
    context = {"booking":booking}
    return render(request, "manage/booking_accept.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def manage_location(request):
    current_user = request.user.id
    location = Location.objects.get(user=current_user)
    today = date.today()
    handle = BookingView.objects.filter(location=location)
    for i in handle:
        if i.date < today and i.status == "XL" and i.status == "M":
            booking = Booking.objects.get(id=i.booking_id)
            booking.status = "TC"
            booking.save()

    form = LocationForm(instance=location)
    if request.method == "POST":
        form = LocationForm(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()
            return redirect("manage_location")
    context = {"form":form}
    return render(request, "manage/location.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def manage_yard(request):
    current_user = request.user.id
    location_id = Location.objects.get(user=current_user)
    yard = Yard.objects.filter(location=location_id)
    context = {"yard":yard}
    return render(request, "manage/yard.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def delete_yard(request,pk):
    yard = Yard.objects.get(id=pk)
    if request.method == "POST":
        yard.delete()
        return redirect("manage_yard")
    context = {"yard":yard}
    return render(request, "manage/delete_yard.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def time_cost(request,pk):
    yard = Yard.objects.get(id=pk)
    time = Time.objects.filter(yard=pk)

    form = AddTimeForm()
    if request.method == "POST":
        form = AddTimeForm(request.POST, yard=yard)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    context = {"time":time, "form":form}
    return render(request, "manage/time.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def delete_timecost(request,pk):
    time = Time.objects.get(id=pk)
    yard = time.yard_id
    if request.method == "POST":
        time.delete()
        return redirect("create_time", pk=yard)
    context = {"time":time}
    return render(request, "manage/delete_time.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def statistical(request):
    current_user = request.user
    location = Location.objects.get(user=current_user)
    revenue = ViewRevenue.objects.get(location=location)
    context = {"revenue":revenue}
    return render(request, "manage/statistic.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['manage'])
def resultData(request):
    timedata = []
    current_user = request.user
    location = Location.objects.get(user=current_user)
    total = ViewChart.objects.filter(location=location)
    for i in total:
        timedata.append({i.time:i.total})
    print(timedata)
    return JsonResponse(timedata, safe=False)
