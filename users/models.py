from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    biography = models.TextField(blank=True)
    vkontakte_url = models.URLField(blank=True)
    telegram_url = models.URLField(blank=True)
    followers = models.ManyToManyField('self', related_name='following', blank=True)

    def __str__(self):
        return f'Profile for {self.user.username}'
