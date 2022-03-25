from django.db import models

# Create your models here.
from cart.models import Order
from customer.models import Customer


class DeliveryLog(models.Model):
    amount = models.FloatField()
    type = models.TextField()
    status = models.TextField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="delivery_log_order")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="delivery_log_customer")
    date = models.DateField()
