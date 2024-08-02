from django.contrib import admin
from .models import Product,Profile
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','item','price','user']


@admin.register(Profile)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','gender','education','dept','address','name','profile']