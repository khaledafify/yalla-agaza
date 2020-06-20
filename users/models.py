from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):

    COUNTRY_EGYPT = "EG"
    COUNTRY_UK = "UK"
    country_choices = (
        (COUNTRY_EGYPT,"Egypt"),
    )
    DEFAULT_COUNTRY = COUNTRY_EGYPT

    GENDER_MALE = "MALE"
    GENDER_FEMALE = "FEMALE"
    GENDER_OTHER = "OTHER"
    GENDER_CHOICES = (
        (GENDER_MALE,"Male"),
        (GENDER_FEMALE,"Female"),
        (GENDER_OTHER,"Other"),
    )

    CURRENCY_EGP = "EGP"
    CURRENCY_CHOICES = (
        (CURRENCY_EGP,"Egyptian Pound"),
    )
    DEFAULT_CURRENCY = CURRENCY_EGP

    avatar = models.ImageField(null=True,blank=True)
    birthdate = models.DateField(null=True,blank=True)
    country = models.CharField(
                               choices=country_choices,
                               default=DEFAULT_COUNTRY,
                               null=False,
                               blank=False,
                               max_length=20)
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        default=DEFAULT_CURRENCY,
        null=False,
        blank = False,
        max_length=3
    )
    gender = models.CharField(
        choices=GENDER_CHOICES ,
        null=True,
        blank=True,
        max_length=7
    )

    is_host = models.BooleanField(default=False)