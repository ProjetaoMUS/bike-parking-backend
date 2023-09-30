from datetime import date

from django.db import models

from django.conf import settings


# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="subscription"
    )
    start_date = models.DateField()
    end_date = models.DateField()

    def is_active(self):
        return self.start_date <= date.today() <= self.end_date