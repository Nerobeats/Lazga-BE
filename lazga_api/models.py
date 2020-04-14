from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    
    TSHIRT="RT"
    HOODIE="HD"
    MUG="MG"
    POPSOCKET="PS"
    POSTER="PR"
    STICKER="ST"
    COASTER="CR"

    TYPES = [
            (TSHIRT, 'tshirt'),
            (HOODIE, 'hoodie'),
            (MUG, 'mug'),
            (POPSOCKET, 'popsocket'),
            (POSTER, 'poster'),
            (STICKER, 'sticker'),
            (COASTER, 'coaster'),
        ]
    type = models.CharField(
        max_length=2,
        choices=TYPES,
        default=TSHIRT,
    )
    name = models.CharField(max_length=150)
    image_url = models.URLField(max_length=200)
    description = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=200)
    itemPrice = models.DecimalField(max_digits=5, decimal_places=2, default= 17.00)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    def __str__(self):
        return self.name
