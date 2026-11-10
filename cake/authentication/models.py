from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.



class RoleChoices(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    USER = 'User', 'User'





class profile(AbstractUser):

    role = models.CharField(max_length=100, choices=RoleChoices.choices, default=RoleChoices.USER)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


    def __str__(self):

        return self.first_name