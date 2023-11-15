from django.db.models.signals import post_save,pre_delete
from django.dispatch import receiver
from .models import Order,Discount,Cart,CustomUser
from decimal import Decimal

@receiver(post_save, sender=Order)
def update_product_sold_count(sender, instance, created,**kwargs):
    if created:
        product = instance.product
        product.sold += 1
        product.product_num-=1
        product.save()
    

@receiver(post_save, sender=Discount)
def update_product_price(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        discount=(instance.discount/Decimal('100'))*product.price
        product.price-=discount
        product.save()
        
@receiver(pre_delete, sender=Discount)
def update_product_price(sender, instance,using, **kwargs):
    product = instance.product
    discount=product.price/(1-instance.discount/Decimal('100'))
    product.price=discount
    product.save()

@receiver(post_save, sender=CustomUser)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        user=instance
        Cart.objects.create(user=user)