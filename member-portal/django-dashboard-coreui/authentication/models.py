# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# from django.contrib.auth.models import User
from django.db.models.base import ModelBase
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from geopy.geocoders import Nominatim

from authentication.countries import COUNTRIES as COUNTRY_CHOICES

OCCUPATIONAL_STATUS_CHOICES = (
    ("", "Occupational Status"),
    ("student", "Student"),
    ("undergraduate student", "Undergraduate Student"),
    ("graduate student", "Graduate Student"),
    ("professional", "Professional"),
)


GENDER_CHOICES = (
    ("", "Gender"),
    ("Male", "Male"),
    ("Female", "Female"),
    ("Prefer Not To Say", "Prefer Not to Say"),
)


class Chapter(models.Model):
    location = models.CharField(max_length=56, null=False, blank=False)
    city = models.CharField(max_length=56, null=False, blank=True)
    country = models.CharField(max_length=56, null=False, blank=True)
    lead = models.CharField(max_length=56, null=False, blank=True)
    foundation = models.DateTimeField(blank=True, default=timezone.now)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    def get_coordinates(self):
        geolocator = Nominatim(user_agent="asrg-app", scheme="http")
        # location = geolocator.geocode(self.city)

        # return (location.latitude, location.longitude)
        return [30, 40]

    def __str__(self):
        return self.location

    class Meta:
        permissions = []


class User(AbstractUser):
    chapter = models.ManyToManyField("Chapter", blank=False, related_name="users")
    # first_name = models.CharField(max_length=25, blank=False)
    # last_name = models.CharField(max_length=25, blank=False)
    gender = models.CharField(
        max_length=25, choices=GENDER_CHOICES, blank=False, default=GENDER_CHOICES[0]
    )
    occupational_status = models.CharField(
        max_length=50,
        choices=OCCUPATIONAL_STATUS_CHOICES,
        blank=False,
        default=OCCUPATIONAL_STATUS_CHOICES[0],
    )
    country = models.CharField(
        max_length=150, choices=COUNTRY_CHOICES, default=COUNTRY_CHOICES[0]
    )

    def __str__(self):
        return self.username
