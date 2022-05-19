from django.test import TestCase
from .models import Product, Brand, ShoppingBasket, Category, Comment
from django.urls import reverse

class ProductTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            title = 'Laptop',
            slug = 'laptop',
        )
        self.brand = Brand.objects.create(
            title = 'Apple',
            slug = 'apple',
        )
        self.product = Product.objects.create(
            title = 'Mac book pro',
            image = 'store_app/114390114.jpg',
            brand = self.brand,
            category = self.category,
            explanation = 'mack book pro is one of the best laptop in the world.',
            price = 2999,
            count = 3,
            available = True,
        )

    def test_product_listing(self):
        self.assertEqual(f'{self.product.title}', 'Mac book pro')
        self.assertEqual(f'{self.product.image}', 'store_app/114390114.jpg')
        self.assertEqual(f'{self.product.brand}', 'Apple')
        self.assertEqual(f'{self.product.category}', 'Laptop')
        self.assertEqual(f'{self.product.explanation}', 'mack book pro is one of the best laptop in the world.')
        self.assertEqual(self.product.price, 2999)
        self.assertEqual(self.product.count, 3)
        self.assertTrue(f'{self.product.available}')

    def test_product_list_view(self):
        response = self.client.get(reverse('store_app:laptop-view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/product-list.html')
        self.assertContains(response, 'Mac book pro')

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_respone = self.client.get('/product/12345')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store_app/products-detail.html')
        self.assertContains(response, 'Mac book pro')


