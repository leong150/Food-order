from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Menu, menuform, Cart, Order
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

# Create your views here.

def restaurant_home(request):
    latest_menu = Menu.objects.order_by('name')
    context = {'latest_menu':latest_menu}
    return render(request, 'restaurant/home_page.html', context)

@login_required(login_url='/accounts/login/')
def order_list(request):
    current_order = Order.objects.last()
    all_order = Order.objects.order_by('order_no').exclude(order_no=current_order.order_no)
    return render(request, 'restaurant/order_list.html', {'all_order':all_order})

def view_order(request, order_no):
    current_order = Order.objects.get(order_no=order_no)
    current_cart = Cart.objects.filter(order=current_order).exclude(qty=0)
    return render(request, 'restaurant/view_order.html', {'current_cart':current_cart, 'current_order':current_order})

def complete_order(request, order_no):
    current_order = Order.objects.get(order_no=order_no)
    current_order.status = request.GET['status'] 
    current_order.save()
    return HttpResponseRedirect(reverse('order_list'))

@login_required(login_url='accounts/login/')
def food_detail(request, menu_id):
    current_menu = Menu.objects.get(pk=menu_id)
    return render(request, 'restaurant/edit_food.html', {'current_menu':current_menu})

@login_required(login_url='accounts/login/')
def edit(request, menu_id):
    current_menu = Menu.objects.get(pk=menu_id)
    form = menuform(request.POST, request.FILES, instance=current_menu)

    if form.is_valid():
        if form.files != {}:
            Menu.objects.get(pk=menu_id).image.delete()
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
        return HttpResponseRedirect(reverse('restaurant_home'))

    else:
        print("error")
        return render(request, 'restaurant/add_food.html')
    
@login_required(login_url='accounts/login/')
def delete(request, menu_id):
    current_menu = Menu.objects.get(pk=menu_id)
    current_menu.delete()
    return HttpResponseRedirect(reverse('restaurant_home'))

def customer_home(request):
    current_order = Order.objects.order_by('order_no').last()
    if current_order is None:
        current_order = Order.objects.create(order_no=1, sum=0)
    latest_menu = Menu.objects.order_by('name')
    context = {'latest_menu':latest_menu, 'current_order':current_order}
    return render(request, 'customer/home_page.html', context)

def selection(request, menu_id):
    current_menu = Menu.objects.get(pk=menu_id)
    current_order = Order.objects.order_by('order_no').last()
    selected_food, created = Cart.objects.get_or_create(menu=current_menu, order=current_order)
    return render(request, 'customer/selection.html', {'selected_food':selected_food})

def addtocart(request, menu_id):
    current_menu = Menu.objects.get(pk=menu_id)
    current_order = Order.objects.order_by('order_no').last()
    selected_food = Cart.objects.get(menu=current_menu, order=current_order)
    selected_food.qty = int(request.POST['qty'])
    selected_food.save()
    return HttpResponseRedirect(reverse('customer_home'))

def see_cart(request):
    current_order = Order.objects.order_by('order_no').last()
    current_cart = Cart.objects.filter(order=current_order).exclude(qty=0)
    current_order.sum = 0
    for x in current_cart:
        current_order.sum += x.menu.price*x.qty
    current_order.save()
    return render(request, 'customer/see_cart.html', {'current_cart':current_cart, 'current_order':current_order})

def place_order(request):
    current_order = Order.objects.order_by('order_no').last()
    Order.objects.create(order_no=current_order.order_no+1, sum=0)
    return render(request, 'customer/confirmed_order.html')