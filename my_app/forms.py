from django import forms
from .models import product
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class product_form(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name','descryption','price','quantity']

class userreggistarationform(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class loginform(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']