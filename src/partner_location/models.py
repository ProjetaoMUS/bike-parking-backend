from django.db import models

# Create your models here.
from django.db import models


class PartnerLocation(models.Model):
    name = models.CharField(max_length=255)
    parking_spaces_count = models.PositiveIntegerField()
    images = models.ImageField(upload_to='partner_location/imagens/', blank=True, null=True)
    address = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
