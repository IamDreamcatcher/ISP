from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, upload_to="photos/profile/", default="photos/profile/default.jpeg")
    address = models.CharField(max_length=100, blank=True)
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return self.user.username
