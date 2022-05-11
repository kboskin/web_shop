from django.db import models

#
# # Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

from catalogue.models import Category
from customer.models import Customer


class Distributor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = PhoneNumberField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category_category")
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE, related_name="product_distributor_distributor")
    amount = models.IntegerField()


class Image(models.Model):
    image_big = models.TextField()
    image_small = models.TextField()
    product = models.ForeignKey(Product, related_name="image_product", on_delete=models.CASCADE)


class Feedback(models.Model):
    product = models.ForeignKey(Product, related_name="feedback_product", on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name="feedback_customer", on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateField()
