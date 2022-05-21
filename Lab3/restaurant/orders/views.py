from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from orders.models import Order


class OrderListView(ListView):
    template_name = "orders/order_list.html"
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


