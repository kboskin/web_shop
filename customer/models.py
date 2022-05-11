from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=80)


# method for updating
@receiver(post_save, sender=User, dispatch_uid=datetime.now().microsecond)
def update_user(created, instance, *args, **kwargs):
    if created:
        Customer.objects.create(user=instance)


class VisitLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visit_log_user")
    activity_type = models.CharField(max_length=30)
    activity_date = models.DateField(auto_now_add=True)
