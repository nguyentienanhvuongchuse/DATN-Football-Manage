from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.forms import inlineformset_factory
from .form import CreateUserForm, BookingYardForm
from yard.models import *
from .filters import LocationFilter, BookingFilter
from .models import *
# Create your views here.

def home(request):
    location = Location.objects.all()
    myFilter = LocationFilter(request.GET, queryset=location)
    location = myFilter.qs
    context = {"location": location, "myFilter":myFilter}
    return render(request, "base/home.html", context)

def detail(request, pk):
    detail = Location.objects.get(id=pk)
    context = {"detail":detail}
    return render(request, "base/detail.html", context)

def time_booking(request,pk):
    current_user = request.user.id
    time = BookingView.objects.filter(location=pk, status="M")
    yard = Yard.objects.filter(location=pk)
    myFilter = BookingFilter(request.GET, queryset=time)
    time = myFilter.qs
    if request.method == "POST":
        booking_id = request.POST["booking_id"]
        data = Booking.objects.get(id=booking_id)
        data.user_id = current_user
        data.status = request.POST["handle"]
        data.save()
    context = {"time":time, "myFilter":myFilter,"yard":yard}
    return render(request, "base/time.html", context)

def booking_yard(request,pk):
    current_user = request.user.id
    location = BookingView.objects.filter(booking=pk)
    booking = Booking.objects.get(id=pk)
    form = BookingYardForm()
    if request.method == "POST":
        form = BookingYardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cart")

    else:
        form = BookingYardForm(initial={"time":time,"user":current_user})
    context = {"time":time, "form":form}
    return render(request,"base/booking_yard.html", context)

def cart(request):
    current_user = request.user
    cart = Booking.objects.filter(user = current_user.id)
    context = {"cart":cart}
    return render(request, "base/order.html", context)

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
