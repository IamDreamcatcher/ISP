from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=40)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    photo = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.name
