from django.urls import path
from django.views.decorators.http import require_GET, require_POST

from product.views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, OrderCreationView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='concrete_product'),
    path('products/<int:pk>/add/', require_POST(OrderCreationView.as_view()), name='make_order'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='concrete_category')
]
