from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=80)


class VisitLog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="visit_log_customer")
    activity_type = models.CharField(max_length=30)
    activity_date = models.DateField(auto_now_add=True)
