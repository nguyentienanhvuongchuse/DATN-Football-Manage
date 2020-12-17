from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.forms import inlineformset_factory
from .form import CreateUserForm, BookingYardForm
from yard.models import *
from .filters import LocationFilter
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
    yard = Yard.objects.filter(location=pk)
    context = {"detail":detail, "yard":yard}
    return render(request, "base/detail.html", context)

def time_booking(request,pk):
    time = Time.objects.filter(yard=pk)
    yard = Yard.objects.get(id=pk)
    context = {"time":time, "yard":yard}
    return render(request, "base/time.html", context)

def booking_yard(request,pk):
    current_user = request.user.id
    time = Time.objects.get(id=pk)
    form = BookingYardForm(initial={"time":time,"user":current_user})
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
