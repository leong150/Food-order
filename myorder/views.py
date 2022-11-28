from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import menu
from django.urls import reverse
from .forms import menuform

# Create your views here.

def home(request):
    latest_menu = menu.objects.order_by('name')
    context = {'latest_menu':latest_menu}
    return render(request, 'myorder/home_page.html', context)

def food_detail(request, menu_id):
    current_menu = menu.objects.get(pk=menu_id)
    return render(request, 'myorder/edit_food.html', {'current_menu':current_menu})

def edit(request, menu_id):
    latest_menu = menu.objects.get(pk=menu_id)
    latest_menu.name = request.POST.get("name")
    latest_menu.price = request.POST.get("price")
    latest_menu.description = request.POST.get("description")
    if request.POST.get("image") == '':
        pass
    else:
        latest_menu.image = (request.POST.get("image"), request.FILES.get("image"))
    latest_menu.save()
    return HttpResponseRedirect(reverse('home'))

def new_food_detail(request):
    return render(request, 'myorder/add_food.html')

def add(request):
    new_menu = menu(name=request.POST.get("name"), price=request.POST.get("price"), description=request.POST.get("description"), image=request.POST.get("image"))
    new_menu.save()
    return HttpResponseRedirect(reverse('home'))