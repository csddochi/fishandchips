from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import User, Category, Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F

# Create your views here.
def introduction(request):
    return render(request, 'fips/introduction.html', {})

def sign_in(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(request.POST)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/main/')
    else: # create a user account
        return sign_up(request, username, password)

def sign_up(request, username, password):
    email = request.POST.get('email')
    _referrer = request.POST.get('referrer')
    if email is not None and _referrer is not None:
        _password = make_password(password)
        _user = User(username=username, email=email, password=_password)
        _user.referrer = _referrer
        _user.save()
        return render(request, 'registration/sign-up.html', {})
    else:
        return render(request, 'registration/login.html', {})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def main_view(request):
    categories = Category.objects.filter().order_by('pk')
    post_list = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    page = request.GET.get('page')

    paginator = Paginator(post_list, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'fips/main.html', {'categories': categories, 'posts':posts})

@login_required
def post_detail(request, pk):
    categories = Category.objects.filter().order_by('pk')
    post = get_object_or_404(Post, pk=pk)
    Post.objects.filter(id=pk).update(hits=F('hits')+1)
    return render(request, 'fips/post_detail.html', {'categories': categories, 'post': post})
