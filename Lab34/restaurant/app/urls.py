from django.urls import path, include, re_path

from app.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', ShowProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/edit/', EditProfileView.as_view(), name='edit_profile'),

    path('profile/<int:pk>/change_password/', PasswordChangingView.as_view(), name='change_password'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z\-]{1,55})/$', AccountActivateView.as_view(),
            name='activate'),
    path('', include('product.urls')),
    path('', include('orders.urls'))
]
