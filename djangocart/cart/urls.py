from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # корзина
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/remove_single/<int:product_id>/', views.cart_remove_single, name='cart_remove_single'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
]