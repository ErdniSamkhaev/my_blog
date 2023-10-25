from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from posts.forms import PostForm
from posts.models import Post
from .forms import UserRegistrationForm, UserLoginForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def dashboard(request):
    posts = Post.objects.filter(author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('dashboard')
    else:
        form = PostForm()

    return render(request, 'users/dashboard.html', {'form': form, 'posts': posts})

