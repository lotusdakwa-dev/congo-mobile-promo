from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .models import Product, Order

def home(request):
    products = Product.objects.all()[:6]
    return render(request, 'core/home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})

def checkout(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        # Logique de commande...
        pass
    return render(request, 'core/checkout.html', {'product': product})

def admin_login_view(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        if pin == settings.ADMIN_DASHBOARD_PIN:
            request.session['admin_authorized'] = True
            return redirect('dashboard')
        else:
            messages.error(request, "Code PIN incorrect !")
    return render(request, 'core/admin_pin.html')

def dashboard_view(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        total_products = Product.objects.count()
        context = {
            'is_admin': False,
            'total_products': total_products,
        }
        return render(request, 'core/visitor_dashboard.html', context)

    if not request.session.get('admin_authorized'):
        return redirect('admin_login')
    
    recent_orders = Order.objects.order_by('-id')[:5]
    total_products = Product.objects.count()
    articles_restants = total_products  
    articles_manquants = Product.objects.filter(stock=0).count() if hasattr(Product, 'stock') else 0
    produits_a_rajouter = 5 

    context = {
        'is_admin': True,
        'recent_orders': recent_orders,
        'total_products': total_products,
        'articles_restants': articles_restants,
        'articles_manquants': articles_manquants,
        'produits_a_rajouter': produits_a_rajouter,
    }
    return render(request, 'core/admin_dashboard.html', context)
from django.shortcuts import get_object_or_404, redirect, render
from .cart import Cart
from .models import Product

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'core/cart_detail.html', {'cart': cart})