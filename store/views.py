from django.shortcuts import render, redirect,get_object_or_404
from param.ipython import message

from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#for registering new users
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def order_success(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'order_success.html', {'product': product})


def complete_order(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        # Here, you can add order logic, e.g., save to an Order model.
        # For now, we simply redirect to a success page.
        return HttpResponseRedirect(reverse('order_success', args=[product_id]))

def order_confirmation(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'order_confirmation.html', {'product': product})

def category(request,categ):
    #replace hyphens with spaces
    categ = categ.replace('-',' ')
    #Grab the category from the url
    try:
        #look up the category
        category = Category.objects.get(name=categ)
        #get the products in that category
        products = Product.objects.filter(category=category)
        return render(request,'category.html',{'products':products,'category':category})
    except:
            messages.error(request, 'Category does not exist')
            return redirect('home')


def product(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product.html', {
        'product': product,
        'room_name': f'product_{product.id}'
    })

def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products':products})


def about(request):
    return render(request,'about.html',{})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.success(request, 'An error occurred .Please try again')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.Thanks for being here')
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are registered successfully')
            return redirect('home')
        else:
            messages.error(request, 'OOPSS!!There was a problem registering')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})



