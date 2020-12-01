from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional.")
    email = forms.EmailField(max_length=254, help_text="Required. Inform a valid email address.")

    class Mata:
        model = User
        fields = ["first_name","last_name","username","email","password1","password2"]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({"class" : "form-control"})
        self.fields["last_name"].widget.attrs.update({"class" : "form-control"})
        self.fields["username"].widget.attrs.update({"class" : "form-control"})
        self.fields["email"].widget.attrs.update({"class" : "form-control"})
        self.fields["password1"].widget.attrs.update({"class" : "form-control"})
        self.fields["password2"].widget.attrs.update({"class" : "form-control"})
