import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView

from orders.constants import ORDER_STATUS_PENDING, ORDER_STATUS_ACTIVE, ORDER_STATUS_DONE
from orders.models import Order

logger = logging.getLogger("main_logger")


class OrderListView(LoginRequiredMixin, ListView):
    template_name = "orders/order_list.html"
    model = Order
    context_object_name = 'orders'
    logger.info("use OrderListView")

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).filter(
            Q(status=ORDER_STATUS_ACTIVE) | Q(status=ORDER_STATUS_DONE)).select_related('user').select_related(
            'product')


class CartView(LoginRequiredMixin, ListView):
    template_name = "orders/cart.html"
    model = Order
    context_object_name = 'orders'
    logger.info("use CartView")

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, status=ORDER_STATUS_PENDING).select_related(
            'user').select_related('product')


class DeleteOrderView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("cart")
    logger.info("use DeleteOrderView")


class DeleteOrderFromHistory(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("orders")
    logger.info("use DeleteOrderFromHistory")


class ClearCartView(LoginRequiredMixin, View):
    def post(self, request):
        logger.info("use ClearCartView")
        cur_user = self.request.user
        Order.objects.filter(user=cur_user, status=ORDER_STATUS_PENDING).delete()

        return HttpResponseRedirect(reverse_lazy("cart"))


class CheckoutView(LoginRequiredMixin, View):
    def post(self, request):
        logger.info("use CheckoutView")
        cur_user = self.request.user
        Order.objects.filter(user=cur_user, status=ORDER_STATUS_PENDING).update(status=ORDER_STATUS_ACTIVE)

        return HttpResponseRedirect(reverse_lazy("cart"))
