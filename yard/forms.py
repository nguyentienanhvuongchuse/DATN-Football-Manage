from django.forms import ModelForm
from django import forms
from .models import *

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
