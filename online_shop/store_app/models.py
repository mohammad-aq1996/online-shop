from django.db import models
from accountapp.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store_app')
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE, related_name='brands')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='categories')
    explanation = RichTextField()
    price = models.IntegerField()
    count = models.SmallIntegerField()
    available = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def buy(self, num):
        """
            Parameter:
                num => number of specific product that a user want to buy
            If count of product(in database) is greater than num, then count of product minus num
            If count of product is less than one it means the product isn't available anymore

        """
        if self.count >= int(num):
            self.count = self.count - int(num)

        if self.count < 1:
            self.available = False

    def count_minus(self):
        """
            If a specific product is available, then it can be reduced
            If the count of a specific product get zero, then turn available to False
        """
        if self.count > 0:
            self.count = self.count - 1
        if self.count == 0:
            self.available = False

    def count_add(self):
        # Increase number of specific product in database and turn available to True
        self.count = self.count + 1
        self.available = True

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
    buyer = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE, related_name='products')
    count = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['buyer']

    def __str__(self):
        return self.product.title


class Comment(models.Model):
    STATUS_CHOICE = [
        ("publish", "Publish"),
        ("draft", "Draft")
    ]
    status = models.CharField(max_length=7, choices=STATUS_CHOICE, default='draft')
    product = models.ForeignKey(Product, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    subject = models.CharField(max_length=25)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['created_at']














