from django.db import models
from django.contrib.auth.models import User
import uuid

class Type (models.Model):
   
    type = models.CharField(
        max_length=50,
        default="tshirt",
    )
    def __str__(self):
        return self.type

class Item(models.Model):

    type = models.ForeignKey(Type , on_delete=models.CASCADE , related_name="items", default =1)
    name = models.CharField(max_length=150, default = "potato")
    image_url = models.URLField(max_length=200,default="https://pbs.twimg.com/profile_images/1046609638425268224/-pJ9ZOS9_400x400.jpg")
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=200)
    itemPrice = models.DecimalField(
        max_digits=5, decimal_places=2, default=17.00)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    color = models.CharField(default="0", max_length=50)
    size = models.CharField(default="0", max_length=50)
    magic = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.order.user.username


class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    products = models.ManyToManyField(Item, through=OrderItem)
    totalPrice = models.DecimalField(max_digits=6, decimal_places=2)
    PREPARING = "PR"
    OUT_FOR_DELIVERY = "OD"
    DELIVERED = "DV"
    CANCELED = "PS"
    NOT_SUBMITTED = "NS"
    TEST = "TS"
    STATUS = [
        (PREPARING, 'preparing order'),
        (OUT_FOR_DELIVERY, 'out for delivery'),
        (DELIVERED, 'delivered'),
        (CANCELED, 'canceled'),
        (NOT_SUBMITTED, 'not submitted'),
        (TEST, 'test'),
    ]
    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default=NOT_SUBMITTED,
    )

    def __str__(self):
        return self.status
