from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import ContactForm
from django.core.mail import send_mail


def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            msg = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail('Contact message', msg, 'from@example.com', [email], fail_silently=True)
            return HttpResponseRedirect(reverse('blog:main'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'blogapp/create.html', context={'form': form})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    #post = Post.objects.get(id=id)
    return render(request, 'blogapp/post.html', context={'post':post})