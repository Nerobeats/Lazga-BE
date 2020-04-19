from django.db import models
from django.contrib.auth.models import User

class Type (models.Model):

    type = models.CharField(
        max_length=50,
        default="tshirt",
    )
    color = models.BooleanField(default = False)
    size = models.BooleanField(default = False)
    magic = models.BooleanField(default = False)
    def __str__(self):
        return self.type


class Item(models.Model):

    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, related_name="items", default=1)
    name = models.CharField(max_length=150, default="")
    image_url = models.URLField(max_length=200, default="")
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=200)
    itemPrice = models.DecimalField(
        max_digits=5, decimal_places=2, default=17.00)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    featured = models.BooleanField(default= False)
    selling_counter = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    color = models.CharField(default="N/A", max_length=50)
    size = models.CharField(default="N/A", max_length=50)
    magic = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return (f'{self.order.user.username}\'s order of {self.item.name} in order {self.order.id}')


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
        return  (f'{self.order.user.username}\'s order #{self.id}')


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE , primary_key = True )
    bio = models.TextField(null = True , blank = True)
    image = models.ImageField(null = True , blank = True)
    favorites = models.ManyToManyField(Item, related_name = "favorites" ,blank = True,default = None , symmetrical = False)
    def __str__(self):
        return (f'{self.user.username}\'s profile')

# class FavoriteItem(models.Model):
#     favorite = models.ForeignKey("Favorite", on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)

#     def __str__(self):
#         return (f'{self.favorite.user.username} has {self.item.name} in favorite list')


# class Favorites(models.Model):
#     user = models.OneToOneField(User ,on_delete=models.CASCADE,primary_key)

#     products = models.ManyToManyField(Item, through=FavoriteItem)

#     def __str__(self):
#         return (f'{self.favorite.user.username}\'s favoirtes list')
#     class Meta:
#         verbose_name_plural = "Favorites"