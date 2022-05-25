import logging

from django.contrib.auth import get_user_model
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from app.models import Profile
from orders.models import Order
from product.models import Product, Category

User = get_user_model()
logging.disable()


class CatalogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password="password")
        self.client = Client(enforce_csrf_checks=False)
        self.client.force_login(self.user)
        self.profile = Profile.objects.create(user=self.user, address="aasfdgdsgdf")

        self.category = Category.objects.create(name='kek')
        self.product = Product.objects.create(name="lol", category=self.category, cost=10)

    def test_order_creation_page(self):
        response = self.client.post(reverse("make_order", kwargs={'pk': self.product.pk}), {"amount": 10})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.all().count(), 1)

    def test_order_creation_page_failure(self):
        response = self.client.post(reverse("make_order", kwargs={'pk': self.product.pk}), {"amount": -5})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.all().count(), 0)
