from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cart.models import Order
from customer.models import Customer


class PaymentLog(models.Model):
    address = models.TextField()
    type = models.TextField()
    status = models.TextField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payment_log_order")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payment_log_customer")
    date = models.DateField(auto_now_add=True)
    request_data = models.TextField()
    response_data = models.TextField()
