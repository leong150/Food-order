from django.contrib import admin

# Register your models here.

from .models import menu, Cart

admin.site.register(menu)
admin.site.register(Cart)