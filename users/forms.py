from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'avatar', 'first_name', 'last_name', 'email', 'phone_number', 'biography',
                  'vkontakte_url', 'telegram_url']  # Добавьте необходимые поля профиля
