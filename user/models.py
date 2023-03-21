from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUser(AbstractUser):
    b_group = models.CharField(max_length=5)
    contact = models.CharField(max_length=10)
