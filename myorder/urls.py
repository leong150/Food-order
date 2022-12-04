from django.urls import path, include
from .import views
from OnlineMenu import settings
from django.conf.urls.static import static
from regex import P
from django.contrib.auth import urls

urlpatterns = [
    
    path('', views.home, name="home"),
    path('new', views.new_food_detail, name="new_food_detail"),
    path('new/add', views.add, name="add"),
    path('<menu_id>', views.food_detail, name="food_detail"),
    path('<menu_id>/edit', views.edit, name="edit"),
    path('accounts/', include('django.contrib.auth.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)