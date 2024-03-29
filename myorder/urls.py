from django.urls import path, include
from .import views
from OnlineMenu import settings
from django.conf.urls.static import static
from regex import P
from django.contrib.auth import urls
from django.views.generic import RedirectView

urlpatterns = [
    
    path('', views.restaurant_home, name="restaurant_home"),
    path('new', views.new_food_detail, name="new_food_detail"),
    path('new/add', views.add, name="add"),
    path('<int:menu_id>', views.food_detail, name="food_detail"),
    path('<int:menu_id>/edit', views.edit, name="edit"),
    path('<int:menu_id>/delete', views.delete, name="delete"),
    path('order/', views.order_list, name="order_list"),
    path('order/<int:order_no>', views.view_order, name="view_order"),
    path('order/<int:order_no>/completeorder', views.complete_order, name="complete_order"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('customer/', views.customer_home, name="customer_home"),
    path('customer/<int:menu_id>', views.selection, name="selection"),
    path('customer/<int:menu_id>/addtocart',views.addtocart, name="addtocart"),
    path('customer/cart', views.see_cart, name="see_cart"),
    path('customer/cart/checkout',views.place_order, name="place_order"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)