from django.forms import ModelForm
from django import forms
from .models import *
from home.models import *

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ["name", "phone", "address", "district","description"]

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class" : "form-control"})
        self.fields["phone"].widget.attrs.update({"class" : "form-control"})
        self.fields["address"].widget.attrs.update({"class" : "form-control"})
        self.fields["district"].widget.attrs.update({"class" : "form-control"})
        self.fields["description"].widget.attrs.update({"class" : "form-control"})

class YardForm(ModelForm):
    class Meta:
        model = Yard
        fields = ["code","type"]

    def __init__(self, *args, **kwargs):
        super(YardForm, self).__init__(*args, **kwargs)
        self.fields["code"].widget.attrs.update({"class" : "form-control"})
        self.fields["type"].widget.attrs.update({"class" : "form-control"})

class CreateYardForm(ModelForm):
    class Meta:
        model = Yard
        fields = ["location","code","type"]

    def __init__(self, *args, **kwargs):
        super(CreateYardForm, self).__init__(*args, **kwargs)
        self.fields["code"].widget.attrs.update({"class" : "form-control"})
        self.fields["type"].widget.attrs.update({"class" : "form-control"})

class TimeCostForm(ModelForm):
    class Meta:
        model = Time
        fields = ["time", "cost"]
    def __init__(self, *args, **kwargs):
        super(TimeCostForm, self).__init__(*args, **kwargs)
        self.fields["time"].widget.attrs.update({"class" : "form-control"})
        self.fields["cost"].widget.attrs.update({"class" : "form-control"})

class AddTimeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.yard = kwargs.pop('yard', None)
        super(AddTimeForm, self).__init__(*args, **kwargs)
        self.fields["time"].widget.attrs.update({"class" : "form-control"})
        self.fields["cost"].widget.attrs.update({"class" : "form-control"})
    def save(self, commit=True):
        time = super().save(commit=False)
        time.yard = self.yard
        time.save()
    class Meta:
        model = Time
        fields = ["time", "cost"]

class HandleBooking(ModelForm):
    class Meta:
        models = Booking
        field = "status"

class BookingYardForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user = self.user
        comment.save()
    class Meta:
        model = Booking
        fields = ["time","date"]
