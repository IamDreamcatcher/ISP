from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    ORDER_STATUS = (
        ("PENDING", "PENDING"),
        ("ACTIVE", "ACTIVE"),
        ("DONE", "DONE")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    status = models.CharField(choices=ORDER_STATUS, default="PENDING", max_length=10)

    def get_cost(self):
        return self.amount * self.product.cost
