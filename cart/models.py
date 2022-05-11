from django.contrib.auth.models import User
from django.db import models

from customer.models import Profile
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_customer")
    created_date = models.DateField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item_cart")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_item_product")
    product_qty = models.IntegerField()


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, related_name="order_cart")
    delivery_type = models.TextField()
    delivery_address = models.TextField()
    order_status = models.TextField()
    last_payment_id = models.ForeignKey(
        'payment.PaymentLog',
        on_delete=models.CASCADE,
        related_name="order_last_payment_id"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="order_customer")
    order_date = models.DateField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_item_order")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_item_product")
    product_qty = models.IntegerField()
