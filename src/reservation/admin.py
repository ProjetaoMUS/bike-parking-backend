from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'date', 'time', 'bike_count']