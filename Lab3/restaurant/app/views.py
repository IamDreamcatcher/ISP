from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from app.forms import RegisterUserForm, LoginUserForm, ProfileForm
from app.models import Profile


class HomePageView(TemplateView):
    template_name = "base/home.html"


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "auth/register.html"

    def form_valid(self, form):
        user = form.save()
        profile = Profile()
        profile.user = user
        user.save()
        profile.save()

        return HttpResponseRedirect(settings.LOGIN_URL)


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = "auth/login.html"


class LogoutUserView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect(settings.LOGIN_URL)


class ShowProfileView(DetailView):
    model = Profile
    template_name = "profile/user_profile.html"
    context_object_name = 'profile'

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class EditProfileView(UpdateView):
    model = Profile
    template_name = "profile/edit_profile.html"
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={'pk': self.kwargs['pk']})


class PasswordChangingView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("home")
    template_name = "profile/change_password.html"
