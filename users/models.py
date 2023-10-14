from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    biography = models.TextField(blank=True)
    vkontakte_url = models.URLField(blank=True)
    telegram_url = models.URLField(blank=True)
    followers = models.ManyToManyField('self', related_name='following', blank=True, symmetrical=False)

    def __str__(self):
        return self.username
