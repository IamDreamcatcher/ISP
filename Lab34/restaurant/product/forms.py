from django.forms import ModelForm

from product.models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', "content", "category", "cost", "photo")


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', "photo")
