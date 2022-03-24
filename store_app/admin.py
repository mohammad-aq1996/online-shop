from django.contrib import admin
from .models import Product, Brand, ShoppingBasket, Category

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ShoppingBasket)
admin.site.register(Category)
