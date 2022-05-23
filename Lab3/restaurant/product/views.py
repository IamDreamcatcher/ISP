from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView, FormView

from orders.forms import OrderCreationForm
from product.models import Product, Category


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product
    context_object_name = 'products'


class CategoryListView(ListView):
    template_name = "products/category_list.html"
    model = Category
    context_object_name = 'categories'


class CategoryDetailView(View):
    template_name = "products/product_list.html"

    def get(self, request, pk):
        products = Product.objects.filter(category_id=pk)
        return render(request, self.template_name, {'products': products})


class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['form'] = OrderCreationForm

        return context


class OrderCreationView(FormView):
    form_class = OrderCreationForm
    template_name = "products/product_detail.html"

    def form_valid(self, form):
        product_id = self.kwargs['pk']
        order = form.save(commit=False)  # commit=False if we need to create filed ourselves
        order.status = "PENDING"
        order.user = self.request.user
        order.product = get_object_or_404(Product, id=product_id)
        order.save()

        return HttpResponseRedirect(reverse_lazy("products"))
