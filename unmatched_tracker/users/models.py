from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateTimeField(blank=True, null=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    is_private = models.BooleanField(default=False)
