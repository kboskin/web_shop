from django.db import models

# Create your models here.
from customer.models import Customer
from product.models import Product
from django.contrib.postgres.fields import ArrayField


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="cart_customer")
    created_date = models.DateField()


class BookedProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="booked_product_cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="booked_product_product")
    qty = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="booked_product_customer")


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name="order_cart")
    delivery_type = models.TextField()
    delivery_address = models.TextField()
    total_items_count = models.IntegerField()
    order_status = models.TextField()
    last_payment_id = models.BigIntegerField()
    products = ArrayField(ArrayField(models.IntegerField()))
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
