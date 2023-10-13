from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),  # имя 'login' задается здесь
    path('register/', views.register, name='register'),
    # другие пути
]
