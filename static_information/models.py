from django.db import models


# Create your models here.

class InformationCategory(models.Model):
    information_cat_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=30)


class InformationItem(models.Model):
    information_cat_id = models.ForeignKey(InformationCategory, on_delete=models.CASCADE)
    content_path = models.CharField(max_length=255)


class InlineInformationItem(models.Model):
    information_cat_id = models.ForeignKey(InformationCategory, on_delete=models.CASCADE)
    content_path = models.ForeignKey(InformationItem, on_delete=models.CASCADE)
    marqup = models.TextField()
