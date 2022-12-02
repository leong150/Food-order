from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import menu, menuform
from django.urls import reverse

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
    form = menuform(request.POST, request.FILES, instance=latest_menu)

    if form.is_valid():
        if form.files != {}:
            menu.objects.get(pk=menu_id).image.delete()
        form.save()
        return HttpResponseRedirect(reverse('home'))

    else:
        print("error")
        return HttpResponseRedirect(reverse('food_detail', args=menu_id))

def new_food_detail(request):
    return render(request, 'myorder/add_food.html')

def add(request):
    new_menu = menu(name=request.POST.get("name"), price=request.POST.get("price"), description=request.POST.get("description"), image=request.POST.get("image"))
    new_menu.save()
    return HttpResponseRedirect(reverse('home'))
