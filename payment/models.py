from django.db import models

# Create your models here.
from cart.models import Order
from customer.models import Customer


class PaymentLog(models.Model):
    address = models.TextField()
    type = models.TextField()
    status = models.TextField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payment_log_order")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="payment_log_customer")
    request_data = models.TextField()
    response_data = models.TextField()
