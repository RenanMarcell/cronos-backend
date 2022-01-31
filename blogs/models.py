from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
