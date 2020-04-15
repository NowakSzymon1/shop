from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    parameters = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    date_added = models.TextField(max_length=200)

