from django.shortcuts import render, get_object_or_404
from .models import Post


def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})


def create_post(request):
    return render(request, 'blogapp/create.html', context={})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    #post = Post.objects.get(id=id)
    return render(request, 'blogapp/post.html', context={'post':post})