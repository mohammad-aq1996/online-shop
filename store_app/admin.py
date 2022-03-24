from django.contrib import admin
from .models import Product, Brand, ShoppingBasket, Category

admin.site.register(Product)
admin.site.register(ShoppingBasket)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}
