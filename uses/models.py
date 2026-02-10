from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=15, default='+996')
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        )
    gender = models.CharField(max_length=100, choices=GENDER, default='MALE')
    city = models.CharField(max_length=100, default='Bishkek')

    def __str__(self):
        return self.username
    
