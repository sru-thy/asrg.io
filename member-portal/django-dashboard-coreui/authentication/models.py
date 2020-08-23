# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelBase
from django.conf import settings


class ChapterMetaClass(ModelBase):
    def __new__(cls, name, bases, attrs):
        klas = super(ChapterMetaClass, cls).__new__(cls, name, bases, attrs)
        for chapter in settings.CHAPTERS:
            location = chapter[0].split('-', 1)[1]
            klas._meta.permissions.append((f'ASRG-{location}', f'ASRG-{location}'))
            klas._meta.permissions.append((f'ASRG-local-lead-{location}', f'ASRG-local-lead-{location}',))

        return klas


class Chapter(models.Model, metaclass=ChapterMetaClass):
    location = models.CharField(
        max_length=24, null=False, blank=False, choices=settings.CHAPTERS, default=settings.CHAPTERS[0]
    )
    city = models.CharField(max_length=56, null=False, blank=True)
    country = models.CharField(max_length=56, null=False, blank=True)
    lead = models.CharField(max_length=56, null=False, blank=True)
    foundation = models.DateTimeField(null=True)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.location

    class Meta:
        permissions = []