from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def categories(request):
    return render(request, 'categories.html')


def authorisation(request):
    return render(request, 'Auth/authorisation.html')


def registration(request):
    return render(request, 'Auth/registration.html')

