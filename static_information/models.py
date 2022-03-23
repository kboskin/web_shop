from django.db import models


# Create your models here.

class InformationCategory(models.Model):
    information_cat = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=30)


class InformationItem(models.Model):
    information_cat = models.ForeignKey(
        InformationCategory,
        on_delete=models.CASCADE,
        related_name="information_category"
    )
    content_path = models.CharField(max_length=255)


class InlineInformationItem(models.Model):
    information_cat = models.ForeignKey(
        InformationCategory,
        on_delete=models.CASCADE,
        related_name="information_category"
    )
    content_path = models.ForeignKey(
        InformationItem,
        on_delete=models.CASCADE,
        related_name="information_item"
    )
    marqup = models.TextField()
