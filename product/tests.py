from django.test import TestCase, Client
from django.urls import reverse

from .models import Product


class ProductAppTests(TestCase):
    # Model Product

    def setUp(self):
        self.product = Product.objects.create(
            name='My Test Product',
            manufacturer='test manufacturer',
            price=9.9,
            quantity=100,
        )

    def test_string_representation(self):
        product = Product(name='My Test Product')
        self.assertEqual(str(product), product.name)

    def test_model_content(self):
        self.assertEqual(f'{self.product.name}', 'My Test Product')
        self.assertEqual(f'{self.product.manufacturer}', 'test manufacturer')
        self.assertEqual(f'{self.product.price}', '9.9')
        self.assertEqual(f'{self.product.quantity}', '100')

    def test_get_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(), '/product/1/')

    # class ViewTests(TestCase):
    # Product Views

    def test_product_url_exists_at_proper_location(self):
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 200)

    def test_product_url_by_name(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
