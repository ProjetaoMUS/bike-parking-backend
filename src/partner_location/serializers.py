from rest_framework import serializers
from .models import PartnerLocation

class PartnerLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerLocation
        fields = '__all__'