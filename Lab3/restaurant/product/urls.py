from django.urls import path

from product.views import ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:product_id>/', ProductListView.as_view(), name='concrete_product')
]
