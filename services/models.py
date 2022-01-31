from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
