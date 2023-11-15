from django.contrib import admin
from django.urls import path,include
from . import views

from django.contrib.auth import views as auth

urlpatterns = [
    path('',views.home_page),
    path('product/<str:pk>/',views.product_detail,name='product'),
    path('product/<str:pk>/add',views.add_to_cart,name='add_to_cart'),
    path('product/filter/<int:filter>',views.filter,name='filter'),
    path('product/filter/<int:filter>',views.filter,name='filter'),

    path('account/',include('django.contrib.auth.urls'),name='login'),
    path('account/signup',views.UserCreationView.as_view(),name='signup'),
    path('logout/', auth.LogoutView.as_view(template_name ='home.html'), name ='logout'),

    path('cart/',views.cart_detail,name='cart'),

    path('order/registration',views.WorkOrderView.as_view(),name='work_order'),
    

]
