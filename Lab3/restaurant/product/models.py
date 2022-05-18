from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    content = models.TextField(blank=True)  # can be empty
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

