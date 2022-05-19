from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from app.forms import RegisterUserForm, LoginUserForm


class HomePage(TemplateView):
    template_name = "base/home.html"


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "auth/register.html"
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "auth/login.html"


class LogoutUser(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect(settings.LOGIN_URL)

