from django.urls import path
from django.views.decorators.http import require_POST

from product.views import *

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='concrete_product'),
    path('products/<int:pk>/add/', require_POST(OrderCreationView.as_view()), name='make_order'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='concrete_category'),
    path('products/new/', CreateProductView.as_view(), name='create_product'),
    path('categories/new/', CreateCategoryView.as_view(), name='create_category'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='update_product'),
    path('categories/<int:pk>/update', UpdateCategoryView.as_view(), name='update_category'),
    path('products/<int:pk>/delete', DeleteProductView.as_view(), name='delete_product'),
    path('categories/<int:pk>/delete', DeleteCategoryView.as_view(), name='delete_category')
]
