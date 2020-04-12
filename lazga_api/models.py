from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=150)
    image_url = models.URLField(max_length=200)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    def __str__(self):
        return self.name

