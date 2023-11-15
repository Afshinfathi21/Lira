from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *
# Register your models here.

class UserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", 'join_date','first_name','last_name','city']
    list_filter = ["city"]
    readonly_fields=['join_date']
    fieldsets = [
        (None, {"fields": ["username", "password"]}),
        ("Personal info", {"fields": ['first_name','last_name','city','address','post_id']}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username",'first_name','last_name','city','address','post_id', "password1", "password2"],
            },
        ),
    ]
    search_fields = ["username",'city']
    ordering = ["city"]

class OrderAdmin(admin.ModelAdmin):
    list_display=['user','total_price_display']
    search_fields=['user']
    list_filter=['user']

    def total_price_display(self, obj):
        return obj.total_price

    total_price_display.short_description = 'Total Price'
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
    list_filter=['name']

class Sub_CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
    list_filter=['name']

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','sold','product_num','brand']
    search_fields=['name','brand']
    list_filter=['price','sold','brand']
class WorkOrderAdmin(admin.ModelAdmin):
    list_display=['user','page_num','total_price_display']
    list_filter=['page_num']

    def total_price_display(self, obj):
        return obj.total_price

    total_price_display.short_description = 'Total Price'
class CityAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']
    list_filter=['name']
class DiscountAdmin(admin.ModelAdmin):
    list_display=['discount','product',]
    search_fields=['discount']
    list_filter=['discount']

    
admin.site.register(CustomUser,UserAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Sub_Category,Sub_CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(WorkOrder,WorkOrderAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(Discount,DiscountAdmin)

