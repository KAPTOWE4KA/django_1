from django.shortcuts import render
from .models import Post


def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})


def create_post(request):
    return render(request, 'blogapp/create.html', context={})
    #TODO видео урок на 48:36. Продолжить дома