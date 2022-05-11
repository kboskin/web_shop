from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from customer.models import Customer


class Notification(models.Model):
    title = models.TextField()
    subtitle = models.TextField()
    content = models.TextField()
    connection_type = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer_notification")
    status = models.TextField()
    date = models.DateField(auto_now_add=True)
    request_data = models.TextField()
    response_data = models.TextField()


class NotificationLog(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_log_customer")
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE,
                                     related_name="notification_log_notification")
