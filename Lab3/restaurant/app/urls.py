from django.urls import path, include

from app.views import HomePage, RegisterUser, LoginUser, LogoutUser

urlpatterns = [
    path('', HomePage.as_view(),  name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('', include('product.urls')),
    path('', include('orders.urls'))
]
