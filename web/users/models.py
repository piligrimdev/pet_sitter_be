from django.db import models
from django.contrib.auth.models import AbstractUser

STANDARD_FIELD_LEN = 255
USER_DETAILS_LEN = 5000


class User(AbstractUser):
    CLIENT = 'client'
    PET_SITTER = 'petsitter'

    STATUS_CHOICES = [
        (CLIENT, 'Client'),
        (PET_SITTER, 'Pet Sitter'),
    ]

    username = models.CharField(
        unique=True,
        max_length=STANDARD_FIELD_LEN,
        verbose_name='Имя пользователя'
    )
    email = models.EmailField(
        unique=True,
        max_length=STANDARD_FIELD_LEN,
        verbose_name='Почта'
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        default=CLIENT
    )
    details = models.TextField(
        blank=True,
        max_length=USER_DETAILS_LEN
    )
