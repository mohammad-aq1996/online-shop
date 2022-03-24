from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store_app')
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE, related_name='brands')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='categories')
    explanation = models.TextField()
    price = models.IntegerField()
    count = models.SmallIntegerField()
    available = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def buy(self, num):
        if self.count >= int(num):
            self.count = self.count - int(num)

        if self.count < 1:
            self.available = False

    def count_minus(self):
        if self.count > 0:
            self.count = self.count - 1
        if self.count == 0:
            self.available = False

    def count_add(self):
        self.count = self.count + 1
        self.available = True

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=12)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=12)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class ShoppingBasket(models.Model):
    buyyer = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE, related_name='products')
    count = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.product.title
