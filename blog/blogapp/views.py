from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from .models import Post, PostForm, Category, CategoryForm, Tag, TagForm
from .forms import ContactForm
from django.core.mail import send_mail


def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})


def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            desc = form.cleaned_data['desc']
            Category.objects.create(name=name, desc=desc)
            return HttpResponseRedirect(reverse('blog:main'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = CategoryForm()
        return render(request, 'blogapp/create.html', context={'form': form})


def tags(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            Tag.objects.create(name=name)
            return HttpResponseRedirect(reverse('blog:main'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = TagForm()
        return render(request, 'blogapp/create.html', context={'form': form})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            category = form.cleaned_data['category']
            tags = form.cleaned_data['tags']
            picture = form.cleaned_data['picture']
            Post.objects.create(name=name, text=text, category=category, picture=picture)
            cur_post = Post.objects.get(name=name)
            cur_post.tags.set(tags)
            cur_post.save()
            return HttpResponseRedirect(reverse('blog:main'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm()
        return render(request, 'blogapp/create.html', context={'form': form})


def post(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        post.delete()
        return HttpResponseRedirect(reverse('blog:main'))
    else:
        post = get_object_or_404(Post, id=id)
        #post = Post.objects.get(id=id)
        return render(request, 'blogapp/post.html', context={'post': post})