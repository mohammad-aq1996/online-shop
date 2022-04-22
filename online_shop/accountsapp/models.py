from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=11)