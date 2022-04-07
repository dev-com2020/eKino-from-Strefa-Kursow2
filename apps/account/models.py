from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


def save(self, *args, **kwargs):
    super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)


mobile_regex = RegexValidator(
    regex=r'^(\+\d{1,3})?,?\s?\d{10,13}',
    message="Numer telefonu powinien mieć format: np. +48543321123")


class CustomerUser(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(validators=[mobile_regex], max_length=13, blank=True)
    photo = models.ImageField(upload_to="profile/", blank=True)
