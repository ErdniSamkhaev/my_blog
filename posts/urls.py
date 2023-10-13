from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('all_list_posts/', views.all_list_posts, name='all_list_posts'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('dislike_post/<int:post_id>/', views.dislike_post, name='dislike_post'),
]
