from django import forms
from .models import Product, Customer
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'digital', 'image']


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'digital', 'image']

class CustomerCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Customer
        fields = ['user', 'name' , 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
