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
