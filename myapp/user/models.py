from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    # null은 0을 포함함, blank는 값이 아예 비어있어도 됨
    name = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)
    registered_date = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name