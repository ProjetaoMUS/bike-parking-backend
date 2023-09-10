from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser model."""

    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = "__all__"

        read_only_fields = ["id", "is_active", "is_staff", "is_superuser"]

    def save(self, **kwargs):
        user = super().save(**kwargs)

        password = self.validated_data.get("password")

        if password is not None:
            user.set_password(password)

        user.save()

        return user
