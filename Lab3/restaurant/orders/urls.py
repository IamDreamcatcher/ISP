from django.urls import path

from orders.views import OrderListView

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='orders')
]
