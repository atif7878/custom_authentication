from django.db import models
from django.utils.translation import gettext_lazy as _


class UserTypeChoices(models.TextChoices):
    LAW_FIRM = 'LAW_FIRM', _('Law Firm')
    TRANSLATION_FIRM = 'TRANSLATION_FIRM', _('Translation Firm')
    STAFF = 'STAFF', _('Staff')
    SUPER_ADMIN = 'SUPER_ADMIN', _('Super Admin')
    END_USER = 'END_USER', _('End User')


class IdentityTypeChoices(models.TextChoices):
    INDIVIDUAL = 'INDIVIDUAL', _('Individual')
    CORPORATE = 'CORPORATE', _('Corporate')


class GenderChoices(models.TextChoices):
    M = 'M', _('Male')
    F = 'F', _('Female')
    O = 'O', _('Other')


class AccountStatusChoices(models.TextChoices):
    ONBOARDING = 'ONBOARDING', _('Onboarding')
    WAITING_FOR_APPROVAL = 'WAITING_FOR_APPROVAL', _('Waiting For Approval')
    APPROVED = 'APPROVED', _('Approved')
    REJECTED = 'REJECTED', _('Rejected')
    DELETED = 'DELETED', _('Deleted')
    ONHOLD = 'ONHOLD', _('Onhold')


class ProfilePictureTypeChoices(models.TextChoices):
    AVATAR = 'AVATAR', _('Avatar')
    LOGO = 'LOGO', _('Logo')


class PictureFrameChoices(models.TextChoices):
    X1 = 'X1', _('1x')
    X2 = 'X2', _('2x')
    X3 = 'X3', _('3x')
    X4 = 'X4', _('4x')
    X5 = 'X5', _('5x')


class GenericStatusChoices(models.TextChoices):
    ACTIVE = 'ACTIVE', _('Active')
    INACTIVE = 'INACTIVE', _('In-Active')
