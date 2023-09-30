from django.conf import settings
from django.db import models

from partner_location.models import PartnerLocation

from .enums import PaymentMethodChoices


class Reservation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reservations"
    )
    location = models.ForeignKey(
        PartnerLocation, on_delete=models.CASCADE, related_name="reservations"
    )

    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    bike_count = models.PositiveIntegerField()
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    payment_method = models.CharField(
        max_length=10,
        choices=PaymentMethodChoices.choices(),
        default=PaymentMethodChoices.CREDIT.name,
    )

    def __str__(self):
        return f"Reservation by {self.user} at {self.location} on {self.start} to {self.end} for {self.bike_count} bikes"
