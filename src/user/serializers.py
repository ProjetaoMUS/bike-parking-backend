from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'tax_id', 'phone_number', 'email', 'first_name', 'gender', 'is_active', 'is_staff', 'is_superuser']
