import json
from django.core import serializers
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import CreateUserForm, CommentForm
from .decorators import *
from yard.models import *
from .filters import LocationFilter, BookingFilter
from .models import *
# Create your views here.

def home(request):
    location = Location.objects.all()
    myFilter = LocationFilter(request.GET, queryset=location)
    location = myFilter.qs

    page = request.GET.get('page')
    paginator = Paginator(location,6)
    try:
        location = paginator.page(page)
    except PageNotAnInteger:
        location = paginator.page(1)
    except EmptyPage:
        location = paginator.page(paginator.num_pages)

    context = {"location": location, "myFilter":myFilter}
    return render(request, "base/home.html", context)

def follow_location(request,obj):

    context = {}
    return render(request, "base/fl_location.html",context)

def detail(request, pk):
    detail = Location.objects.get(id=pk)
    comment = Comment.objects.filter(location=pk, reply__isnull=True).order_by("-date")
    rating = Rating.objects.get(location=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            content = request.POST.get("body")
            reply_id = request.POST.get("comment_id")
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(author_id=request.user.id, location_id=pk, body=content, reply=comment_qs)
            comment.save()
            messages.info(request, 'Thao tác thành công, cảm ơn ban!')
            return HttpResponseRedirect(request.path)
    context = {"detail":detail,"comment":comment, "form":form, "rating":rating}
    return render(request, "base/detail.html", context)

def rate(request):
    if request.method == "POST":
        el_id = request.POST.get("el_id")
        val = request.POST.get("val")
        obj = Rating.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({"success":"true", "score":val}, safe=False)
    return JsonResponse({"success":"false"})

@login_required(login_url="login")
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

@login_required(login_url="login")
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

@login_required(login_url="login")
def cart(request):
    current_user = request.user.id
    cart = CartView.objects.filter(user_booking=current_user, status="XL")
    total = 0
    for gt in cart:
        total += int(gt.cost)
    if request.method == "POST":
        booking_id = request.POST["booking_id"]
        data = Booking.objects.get(id=booking_id)
        data.status = request.POST["handle"]
        data.save()
    context = {"cart":cart, "total":total}
    return render(request, "base/order.html", context)

@login_required(login_url="login")
def cart_history(request):
    current_user = request.user.id
    cart = CartView.objects.filter(user_booking=current_user)
    context = {"cart":cart}
    return render(request, "base/cart_history.html", context)

def contact(request):
    context = {}
    return render(request, "base/contact.html",context)

def sendEmai(request):
    if request.method == 'POST':
        template = render_to_string('base/email_template.html',
        {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['sp.mysite2020@gmail.com'],
        )
        email.fail_silently = False
        email.send()
    return render(request,'base/email_send.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request, 'Tài khoản hoặc mật khẩu không hợp lệ')
    context = {}
    return render(request, "base/login.html", context)

@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("home")

def signup(request):
    if request.method == "POST":
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        password = request.POST["password"]

        usr = User.objects.create_user(username,email,password)
        usr.first_name = fname
        usr.last_name = lname
        usr.save()
        register = DetailUser(user=usr, phone=phone, address=address)
        register.save()
        login(request, usr)
        return redirect('home')
    context = {}
    return render(request, "base/signup.html", context)

@login_required(login_url="login")
def information(request):
    current_user = request.user.id
    user = User.objects.get(id = current_user)
    detail = DetailUser.objects.get(user_id=current_user)
    if request.method == "POST":
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()

        detail.phone = phone
        detail.address = address
        detail.save()
        print(request.POST)
    context = {"user":user, "detail":detail}
    return render(request, "base/user.html",context)

@login_required(login_url="login")
def change_pw(request):
    current_user = request.user.id
    user = User.objects.get(id = current_user)
    if request.method == "POST":
        password = request.POST["password"]
        print(password)
        print(user.password)
        user.set_password = password
        print(user.password)
        user.save()
        print(user.password)
        update_session_auth_hash(request, user)
    context = {"user":user}
    return render(request, "base/change_pw.html",context)

#Location

def thanhkhe(request):
    location = Location.objects.filter(district="TK")
    context = {"location":location}
    return render(request, "district/thanhkhe.html",context)

def sontra(request):
    location = Location.objects.filter(district="ST")
    context = {"location":location}
    return render(request, "district/sontra.html",context)

def nhs(request):
    location = Location.objects.filter(district="NHS")
    context = {"location":location}
    return render(request, "district/nhs.html",context)

def lienchieu(request):
    location = Location.objects.filter(district="LC")
    context = {"location":location}
    return render(request, "district/lienchieu.html",context)

def haichau(request):
    location = Location.objects.filter(district="HC")
    context = {"location":location}
    return render(request, "district/haichau.html",context)

def camle(request):
    location = Location.objects.filter(district="CL")
    context = {"location":location}
    return render(request, "district/camle.html",context)

def hoavang(request):
    location = Location.objects.filter(district="ST")
    context = {"location":location}
    return render(request, "district/hoavang.html",context)
