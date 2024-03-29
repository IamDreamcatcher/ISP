from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from app.models import Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', "address", "phone")
