from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cart.models import Order
from customer.models import Customer


class DeliveryLog(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="delivery_log_order")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="delivery_log_user")
    amount = models.FloatField()
    type = models.TextField()
    status = models.TextField()
    date = models.DateField(auto_now_add=True)
    request_data = models.TextField()
    response_data = models.TextField()
