from django.conf import settings
from django.db import models

from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.PositiveIntegerField()

    def get_cost(self):
        return self.cost * self.amount
