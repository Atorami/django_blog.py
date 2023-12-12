from django.contrib.auth import authenticate, login, logout
from django.contrib.postgres.search import SearchVector
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SearchForm, LoginForm, CommentForm
from .models import Post, Comment


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
            results = Post.objects.annotate(search=SearchVector('title', 'body')).filter(search=query)

    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
        else:
            form = LoginForm()

        return render(request, 'Auth/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'Auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


def user_profile(request):
    return render(request, 'Profile/profile.html')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request, 'Posts/post_detail.html', {'post': post, 'comments': comments, 'form': form})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        comment.delete()
    return redirect('post_detail', pk=comment.post.id)

