from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.http.response import HttpResponse


def welcome(request):
    """Представление для демонстрации приветственной страницы. Рендеринг."""
    return render(request, 'posts/welcome.html')


def post_list(request):
    """Функция представления для отображения всех постов. Извлекает все объекты Post из базы данных и передает их в
    шаблон."""
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        return redirect('posts')
    return render(request, 'posts/create_post.html')


def all_list_posts(request):
    return HttpResponse(request, 'posts/all_list_posts.html')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes.add(request.user)
    return redirect('posts-index')


@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.dislikes.add(request.user)
    return redirect('posts-index')

