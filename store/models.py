from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
# Create your models here.


    



class City(models.Model):
    name=models.CharField( max_length=100)
    def __str__(self) -> str:
        return self.name
    

class Sub_Category(models.Model):
    name=models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=100)
    sub_category=models.ForeignKey(Sub_Category, on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Sub_Category, on_delete=models.CASCADE,null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    brand=models.CharField(max_length=200,default='نامعلوم')
    product_num=models.PositiveIntegerField(default=1)
    sold=models.PositiveIntegerField(default=0)
    img=models.ImageField(upload_to='products/%Y%m%d')
    description=models.TextField()
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.name
    

class CustomUser(AbstractUser):
    address=models.TextField(null=True,blank=True)
    city=models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    post_id=models.CharField(max_length=10,null=True,blank=True)
    join_date=models.DateTimeField(auto_now_add=True)



    
class Cart(models.Model):
    user=models.OneToOneField(CustomUser ,on_delete=models.CASCADE,null=True)
    product=models.ManyToManyField(Product)
    def __str__(self):
        if self.user:
            return f'Cart for {self.user.username}'
        else:
            return 'NA'





class Order(models.Model):
    product=models.ManyToManyField( Product)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post_price=models.DecimalField(max_digits=5, decimal_places=2,default=40)
    


    @property
    def total_price(self):
        product_price=list(Order.objects.values('product__price'))[0]['product__price']
        total_price=product_price+self.post_price

        return total_price



class WorkOrder(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    page_num=models.PositiveIntegerField()
    description=models.TextField()
    file=models.FileField( upload_to='orders/%Y%m%d/',validators=[FileExtensionValidator(['txt','pdf','docx','pptx'])],null=True)

    @property
    def total_price(self):
        page_price=1
        t_p=self.page_num*page_price
        return t_p
    
    def __str__(self) -> str:
        return self.user.username


class Discount(models.Model):
    discount=models.PositiveIntegerField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
