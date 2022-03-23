from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    category_description = models.CharField(max_length=30)
    parent_category_id = models.ForeignKey("self", on_delete=models.CASCADE)


class StaticItem(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    html_content = models.TextField()


class Catalogue(models.Model):
    categories = ArrayField(models.IntegerField(blank=True), blank=True)
