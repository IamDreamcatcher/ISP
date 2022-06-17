import logging

from django.contrib.auth import get_user_model
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from app.models import Profile
from product.models import Product, Category
from .models import Order

User = get_user_model()
logging.disable()


class OrderTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password="password")
        self.client = Client(enforce_csrf_checks=False)
        self.client.force_login(self.user)
        self.profile = Profile.objects.create(user=self.user, address="aasfdgdsgdf")

        self.category = Category.objects.create(name='kek')
        self.product = Product.objects.create(name="lol", category=self.category, cost=10)
        self.order = Order.objects.create(user=self.user, product=self.product, amount=10)

    def test_orders_page_status_code(self):
        response = self.client.get(reverse('orders'))
        self.assertEqual(response.status_code, 200)

    def test_cart_page_status_code(self):
        response = self.client.get(reverse('cart'))
        self.assertEqual(response.status_code, 200)

    def test_order_delete_page(self):
        response = self.client.post(reverse("delete_order_from_history", kwargs={'pk': self.order.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.all().count(), 0)

    def test_cart_clear_page(self):
        response = self.client.post(reverse("clear_cart"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.all().count(), 0)

    def test_checkout_page(self):
        response = self.client.post(reverse("checkout"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.all().count(), 1)
