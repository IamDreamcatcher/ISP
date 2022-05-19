from django.shortcuts import render
from django.views.generic import ListView

from product.models import Product


class ProductListView(ListView):
    template_name = "products/product_list.html"
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category')
