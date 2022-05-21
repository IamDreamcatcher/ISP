from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from product.models import Product, Category


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"
    model = Product
    context_object_name = 'product'


class CategoryListView(ListView):
    template_name = "products/category_list.html"
    model = Category
    context_object_name = 'categories'


class CategoryDetailView(View):
    template_name = "products/product_list.html"

    def get(self, request, pk):
        products = Product.objects.filter(category_id=pk)
        return render(request, self.template_name, {'products': products})
