from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    category_description = models.CharField(max_length=30)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, related_name="category_parent_category")
    is_active = models.BooleanField(default=False)


class StaticItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    html_content = models.TextField()
