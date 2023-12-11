from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import SearchForm, LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from django.contrib.auth import authenticate, login, logout


def index(request):
    query = request.GET.get('q')
    if query:
        posts_list = Post.objects.filter(title__icontains=query)
    else:
        posts_list = Post.objects.all()

    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(request, 'index.html', {'posts': posts, 'query': query})


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


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.annotate(search=SearchVector('title', 'body')).filter(search=query   )

    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index', {'user': user})
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
        else:
            form = LoginForm()
        return render(request, 'Auth/authorisation.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')
