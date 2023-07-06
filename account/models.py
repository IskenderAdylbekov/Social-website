from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse

from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    country = CountryField(blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"username": self.username})

    def __str__(self) -> str:
        return self.username


class Contact(models.Model):
    user_from = models.ForeignKey(
        CustomUser, related_name="rel_from_set", on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        CustomUser, related_name="rel_to_set", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["-created"])]
        ordering = ["created"]

    def __str__(self) -> str:
        return f"{self.user_from} follows{self.user_to}"


user_model = get_user_model()
user_model.add_to_class(
    "following",
    models.ManyToManyField(
        "self", through=Contact, related_name="followers", symmetrical=False
    ),
)
