from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from .models import *
from .forms import *

from rest_framework.views import APIView


# Create your views here.
def home_page(request):
    products=Product.objects.all()
    context={'products':products}
    user=CustomUser.objects.get(id=1)
    return render(request,'home.html',context)


def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    context={
        'product':product
    }
    return render(request,'product.html',context)

def add_to_cart(request,pk):
    product=Product.objects.get(pk=pk)
    u=request.user
    user=CustomUser.objects.get(pk=u.id)
    user.cart.product.add(product)
    products=user.cart.product.all()
    context={
    'products':products,
    }
    return render(request,'orders_list.html',context)
    

class UserCreationView(APIView):
    def get(self,request):
        form=UserCreationForm
        return render(request,'registration/signup.html',context={'form':form})
    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user=user)
            return render(request,'successfully_created.html')
        else:
            return render(request,'registration/signup.html',context={'form':form})

def cart_detail(request):
    user_id=request.user.id
    user=CustomUser.objects.get(pk=user_id)
    products=user.cart.product.all()
    context={
    'products':products,
    }
    return render(request,'orders_list.html',context)

class WorkOrderView(APIView):
    def get(self,request):
        form=WorkOrderForm
        return render(request,'work_order.html',context={'form':form})
    
    def post(self,request):
        form=WorkOrderForm(request.POST,request.FILES)
        form.instance.user=request.user
        if form.is_valid():
            form.save()
            return render(request,'order_submit.html')
        else:
            print('not valid')
            return render(request,'work_order.html',context={'form':form})


def filter(request,filter):
    pass