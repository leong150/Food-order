from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import menu, menuform, Cart
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

# Create your views here.

def restaurant_home(request):
    latest_menu = menu.objects.order_by('name')
    context = {'latest_menu':latest_menu}
    return render(request, 'restaurant/home_page.html', context)

@login_required(login_url='accounts/login/')
def food_detail(request, menu_id):
    current_menu = menu.objects.get(pk=menu_id)
    return render(request, 'restaurant/edit_food.html', {'current_menu':current_menu})

@login_required(login_url='accounts/login/')
def edit(request, menu_id):
    current_menu = menu.objects.get(pk=menu_id)
    form = menuform(request.POST, request.FILES, instance=current_menu)

    if form.is_valid():
        if form.files != {}:
            menu.objects.get(pk=menu_id).image.delete()
        form.save()
        return HttpResponseRedirect(reverse('restaurant_home'))

    else:
        print("error")
        return HttpResponseRedirect(reverse('food_detail', args=menu_id))

@login_required(login_url='accounts/login/')
def new_food_detail(request):
    return render(request, 'restaurant/add_food.html')

@login_required(login_url='accounts/login/')
def add(request):
    form = menuform(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))

    else:
        print("error")
        return render(request, 'restaurant/add_food.html')

def customer_home(request):
    current_cart = Cart.objects.order_by('order_no').last()
    latest_menu = menu.objects.order_by('name')
    context = {'latest_menu':latest_menu, 'current_cart':current_cart}
    return render(request, 'customer/home_page.html', context)

def selection(request, menu_id):
    current_menu = menu.objects.get(pk=menu_id)
    return render(request, 'customer/selection.html', {'current_menu':current_menu})

def addtocart(request, menu_id):
    current_cart = Cart.objects.order_by('order_no').last()
    current_menu = menu.objects.get(pk=menu_id, cart=current_cart)
    current_menu.qty = int(request.POST['qty'])
    current_menu.save()
    return HttpResponseRedirect(reverse('customer_home'))

def see_cart(request, cart_no):
    cart = get_object_or_404(Cart, order_no=cart_no)
    current_order = cart.menu_set.filter(qty__gte=1)
    cart.sum = 0
    for x in current_order:
        cart.sum += x.price*x.qty
    cart.save()
    return render(request, 'customer/see_cart.html', {'current_order':current_order,'cart':cart})

def place_order(request, cart_no):
    Cart.objects.create(order_no=cart_no+1, sum=0)
    return render(request, 'customer/confirmed_order.html')