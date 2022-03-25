from django.contrib import admin
from .models import Product, Brand, ShoppingBasket, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'count', 'available']


@admin.register(ShoppingBasket)
class ShoppingBasketAdmin(admin.ModelAdmin):
    list_display = ['product', 'buyyer', 'count']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}
