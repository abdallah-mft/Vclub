from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    wilaya = models.CharField(max_length=50, blank=True, null=True)
    university = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    year_of_study = models.PositiveIntegerField(blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return self.username 
    
