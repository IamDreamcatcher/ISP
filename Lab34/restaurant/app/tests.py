import logging

from django.contrib.auth import get_user_model
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from .models import Profile

User = get_user_model()
logging.disable()


class AuthTests(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password="password")
        self.client = Client(enforce_csrf_checks=False)
        self.client.force_login(self.user)

        self.profile = Profile.objects.create(user=self.user, address="aasfdgdsgdf")

    def test_base_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_logout_page_status_code(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_profile_page(self):
        response = self.client.get(reverse("profile", kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, 200)

    def test_profile_page_edit(self):
        response = self.client.post(reverse("edit_profile", kwargs={'pk': self.profile.pk}),
                                    {'address': "fafaaafaffafa"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Profile.objects.get(pk=self.profile.pk).address, "fafaaafaffafa")


class SignUpPageTests(TestCase):

    def setUp(self):
        self.username = 'new_user'
        self.password1 = 'clown31411sasgahjgf'
        self.password2 = 'clown31411sasgahjgf'

    def test_signup_page_status_code(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        response = self.client.post(reverse('register'), {'username': self.username, 'password1': self.password1,
                                                          'password2': self.password2})

        self.assertEqual(Profile.objects.all().count(), 1)
        self.assertEqual(response.status_code, 302)

    def test_signup_form_failure(self):
        response = self.client.post(reverse('register'), {'username': self.username, 'pasdadsword1': self.password1})
        self.assertEqual(Profile.objects.all().count(), 0)
