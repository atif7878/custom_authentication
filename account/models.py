import phonenumbers
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from account.enums import GenderChoices


class CustomUserManager(BaseUserManager):
    def create_user(self, mobile_number, password=None, **extra_fields):
        if not mobile_number:
            raise ValueError(_('The Mobile Number field must be set'))

        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password=None, **extra_fields):
        user = self.create_user(mobile_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(null=True, blank=True, verbose_name=_('Email Address'))
    mobile_number = PhoneNumberField(unique=True, verbose_name=_('Mobile Number'))
    full_name = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Full Name'))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_('Date of Birth'))
    gender = models.CharField(max_length=2, choices=GenderChoices.choices, default=GenderChoices.M, verbose_name=_('Gender'))

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.full_name if self.full_name is not None else str(self.mobile_number)

    def save(self, *args, **kwargs):
        parsed_number = phonenumbers.parse(str(self.mobile_number), None)
        normalized_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        self.phone_number = normalized_number
        super(User, self).save(*args, **kwargs)
