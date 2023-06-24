from django.db import models
from django.contrib.auth.models import AbstractUser

from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    country = CountryField(blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self) -> str:
        return f"Profile of {self.username}"
