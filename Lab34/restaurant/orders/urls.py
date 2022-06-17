from django.urls import path

from orders.views import *

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>', DeleteOrderFromHistory.as_view(), name='delete_order_from_history'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:pk>', DeleteOrderView.as_view(), name='delete_order_from_cart'),
    path('cart/clear', ClearCartView.as_view(), name='clear_cart'),
    path('cart/checkout', CheckoutView.as_view(), name='checkout')
]
