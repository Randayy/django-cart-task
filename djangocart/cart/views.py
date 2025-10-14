from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from cart.cart import Cart
from cart.models import Product
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    available_only = request.GET.get('available') == 'true'
    category_slug = request.GET.get('category')

    products = Product.objects.all()
    categories = Category.objects.all()

    if available_only:
        products = products.filter(available=True)

    if category_slug:
        products = products.filter(category__slug=category_slug)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'available_only': available_only,
        'selected_category': category_slug,
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')

def cart_remove_single(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove_single(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/cart_detail.html', {'cart': cart})

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart_detail')

