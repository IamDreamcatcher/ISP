import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from orders.forms import OrderCreationForm
from orders.models import Order
from product.models import Product, Category

logger = logging.getLogger("main_logger")


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product
    context_object_name = 'products'
    logger.info("use ProductListView")


class CategoryListView(ListView):
    template_name = "products/category_list.html"
    model = Category
    context_object_name = 'categories'
    logger.info("use CategoryListView")


class CategoryDetailView(ListView):
    template_name = "products/category_detail.html"
    model = Product
    context_object_name = 'products'
    logger.info("use CategoryDetailView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']

        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk']).select_related('category')


class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"
    model = Product
    context_object_name = 'product'
    logger.info("use ProductDetailView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderCreationForm

        return context


class OrderCreationView(LoginRequiredMixin, FormView):
    form_class = OrderCreationForm
    template_name = "products/product_detail.html"

    def form_valid(self, form):
        logger.info("use OrderCreationView")

        product_id = self.kwargs['pk']
        order = form.save(commit=False)  # commit=False if we need to create filed ourselves
        order.status = "PENDING"
        order.user = self.request.user
        order.product = get_object_or_404(Product, id=product_id)
        exists_order = Order.objects.filter(user=order.user, product=order.product, status="PENDING")
        if exists_order:
            exists_order[0].amount += order.amount
            exists_order[0].save()
        else:
            order.save()

        return HttpResponseRedirect(reverse_lazy("products"))

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse_lazy("products"))
