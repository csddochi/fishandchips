from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Category, Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from .forms import PostForm, CommentForm

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
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
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

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'fips/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'fips/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('main')

@login_required
def noti_view(request):
    categories = Category.objects.all().order_by('pk')
    category = Category.objects.filter(id=1) #1 notification
    post_list = Post.objects.filter(
        subject=category
    ).filter(
        published_date__lte=timezone.now()
    ).order_by(
        '-published_date'
    )
    page = request.GET.get('page')

    paginator = Paginator(post_list, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'fips/noti_list.html', {'categories': categories, 'posts':posts})

@login_required
def fnfc_view(request):
    categories = Category.objects.all().order_by('pk')
    category = Category.objects.filter(id=4) #4 fanfic-board
    post_list = Post.objects.filter(
        subject=category
    ).filter(
        published_date__lte=timezone.now()
    ).order_by(
        '-published_date'
    )
    page = request.GET.get('page')

    paginator = Paginator(post_list, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'fips/fnfc_list.html', {'categories': categories, 'posts':posts})

@login_required
def free_view(request):
    categories = Category.objects.all().order_by('pk')
    category = Category.objects.filter(id=2) #2 free-board
    post_list = Post.objects.filter(
        subject=category
    ).filter(
        published_date__lte=timezone.now()
    ).order_by(
        '-published_date'
    )
    page = request.GET.get('page')

    paginator = Paginator(post_list, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'fips/free_list.html', {'categories': categories, 'posts':posts})

@login_required
def file_view(request):
    categories = Category.objects.all().order_by('pk')
    category = Category.objects.filter(id=3) #3 file-board
    post_list = Post.objects.filter(
        subject=category
    ).filter(
        published_date__lte=timezone.now()
    ).order_by(
        '-published_date'
    )
    page = request.GET.get('page')

    paginator = Paginator(post_list, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'fips/file_list.html', {'categories': categories, 'posts':posts})

@login_required
def stry_view(request):
    categories = Category.objects.all().order_by('pk')
    category = Category.objects.filter(id=5) #5 story-board
    post_list = Post.objects.filter(
        subject=category
    ).filter(
        published_date__lte=timezone.now()
    ).order_by(
        '-published_date'
    )
    page = request.GET.get('page')

    paginator = Paginator(post_list, 15)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'fips/stry_list.html', {'categories': categories, 'posts':posts})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'fips/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
