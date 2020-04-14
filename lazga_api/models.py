from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=150)
    image_url = models.URLField(max_length=200)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=50) # shouldn't this have choices?
    tags = models.CharField(max_length=200) # shouldn't this also have choices?
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1 ) # add a related_name
    def __str__(self):
        return self.name

