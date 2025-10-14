from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.api.shop_api import ProductViewSet, CategoryViewSet
from cart.api.cart_api import CartAPIView


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartAPIView.as_view(), name='cart'),
    path('cart/<int:product_id>/', CartAPIView.as_view(), name='cart-delete'),
]
