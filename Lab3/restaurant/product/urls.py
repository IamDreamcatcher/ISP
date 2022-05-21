from django.urls import path

from product.views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='concrete_product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='concrete_category')
]
