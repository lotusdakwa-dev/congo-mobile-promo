from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart_detail, name='cart_detail'),
    
    
]