from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def index(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
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