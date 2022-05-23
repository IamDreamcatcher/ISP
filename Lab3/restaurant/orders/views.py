from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView

from orders.models import Order


class OrderListView(ListView):
    template_name = "orders/order_list.html"
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).filter(Q(status="ACTIVE") | Q(status="DONE"))


class CartView(ListView):
    template_name = "orders/cart.html"
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, status="PENDING")


class DeleteOrderView(DeleteView):
    model = Order
    success_url = reverse_lazy("cart")


class ClearCartView(View):
    def post(self, request):
        cur_user = self.request.user
        Order.objects.filter(user=cur_user, status="PENDING").delete()

        return HttpResponseRedirect(reverse_lazy("cart"))


class CheckoutView(View):
    def post(self, request):
        cur_user = self.request.user
        Order.objects.filter(user=cur_user, status="PENDING").update(status="ACTIVE")

        return HttpResponseRedirect(reverse_lazy("cart"))
