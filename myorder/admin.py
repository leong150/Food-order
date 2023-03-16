from django.contrib import admin

# Register your models here.

from .models import Order, Menu, Cart

admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Cart)