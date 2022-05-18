from django.urls import path, re_path

from app.views import index

urlpatterns = [
    path('', index,  name='home'),
]
