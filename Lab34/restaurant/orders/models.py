from django.contrib.auth.models import User
from django.db import models

from orders.constants import ORDER_STATUSES
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    status = models.CharField(choices=ORDER_STATUSES, default="PENDING", max_length=10)

    def get_cost(self):
        return self.amount * self.product.cost
