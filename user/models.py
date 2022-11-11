from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomerUser(AbstractUser):
    phone = models.CharField(default = '', max_length = 16)
    adress = models.CharField(default = '', max_length = 200)