from __future__ import annotations

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_cpf_cnpj.fields import CPFField
from phonenumber_field.modelfields import PhoneNumberField

from .enums import *
from .exceptions import *


class CustomUserManager(BaseUserManager):
    def _create_user(
        self,
        email: str,
        password: str,
        tax_id: str,
        first_name: str,
        gender: str,
        is_active: bool = True,
        is_staff: bool = False,
        is_superuser: bool = False,
        **extra_fields,
    ) -> CustomUser:
        """Used as a helper method for creating a user."""
        if tax_id is None:
            raise NullTaxIdError("Tax ID cannot be null.")

        UserModel = self.model

        user = UserModel(
            email=email,
            tax_id=tax_id,
            first_name=first_name,
            gender=gender,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.password = make_password(password)
        user.save(using=self.db)
        return user

    def create_user(
        self,
        email: str,
        password: str,
        tax_id: str,
        first_name: str,
        gender: str,
        **extra_fields,
    ) -> CustomUser:
        """Creates a user."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        return self._create_user(
            email=email,
            password=password,
            tax_id=tax_id,
            first_name=first_name,
            gender=gender,
            **extra_fields,
        )

    def create_superuser(
        self,
        email: str,
        password: str,
        tax_id: str,
        first_name: str,
        gender: str,
        **extra_fields,
    ):
        """Creates a superuser."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            email=email,
            password=password,
            tax_id=tax_id,
            first_name=first_name,
            gender=gender,
            **extra_fields,
        )


class CustomUser(AbstractBaseUser):
    """User model."""

    class Meta:
        verbose_name = _("user")

    objects = CustomUserManager()

    tax_id = CPFField("tax_id", unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(
        "phone_number", unique=True, null=False, blank=False
    )
    email = models.EmailField("email", unique=True, null=True, blank=False)
    first_name = models.CharField("first_name", max_length=30, blank=False, null=False)
    gender = models.CharField(
        "gender", choices=GENDERS, max_length=16, blank=False, null=False
    )

    is_active = models.BooleanField("active", default=True)
    is_staff = models.BooleanField("staff", default=False)
    is_superuser = models.BooleanField("superuser", default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["tax_id", "phone_number", "first_name", "gender"]

    def __str__(self) -> str:
        return self.email

    def __repr__(self) -> str:
        return f"CustomUser({self.email})"
