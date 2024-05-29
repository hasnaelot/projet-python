from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductUpdateForm, CustomerCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *

# Create your views here.

@login_required
def store(request):
     products = Product.objects.all()
     context = {'products':products}
     return render(request, 'shopping/store.html', context)

def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
     else:
          items = []
          order = {'get_cart_total':0, 'get_cart_items':0}

     context = {'items':items, 'order':order}
     return render(request, 'shopping/cart.html', context)

def checkout(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
     else:
          items = []
          order = {'get_cart_total':0, 'get_cart_items':0}

     context = {'items':items, 'order':order}
     return render(request, 'shopping/checkout.html', context)

def home(request):
     context = {}
     return render(request, 'shopping/home.html', context)

def updateItem(request):
     return JsonResponse('Item was added', safe=False)

def signup(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('product_list')
            return redirect('login')
    else:
        form = CustomerCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the product list page after login
                return redirect('home')
            else:
                # Invalid login
                return render(request, 'registration/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
