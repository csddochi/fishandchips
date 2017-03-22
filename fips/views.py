
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Category, Post, Comment, UploadFile, ImageComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F
from .forms import PostForm, CommentForm, UploadFileForm, ImageCommentForm
import os
from django.db import IntegrityError

# Create your views here.
def introduction(request):
    return render(request, 'fips/introduction.html', {})

def sign_in(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(request.POST)
    if username is '':
        return render(request, 'registration/login.html', {})
    else:
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/main/')
        else: # create a user account
            try:
                return sign_up(request, username, password)
            except IntegrityError:
                return HttpResponseRedirect('/login/')

def sign_up(request, username, password):
    email = request.POST.get('email')
    _referrer = request.POST.get('referrer')
    print('referrer:', _referrer)
    referrers = str(_referrer).split('-')
    for r in referrers:
        if not User.objects.filter(ref_code__exact=r):
            return HttpResponseRedirect('/')
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
    if post.author != request.user:
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
    upload_list = UploadFile.objects.all().filter(
        published_date__lte=timezone.now()
    ).order_by(
        '-published_date'
    )
    page = request.GET.get('page')

    paginator = Paginator(upload_list, 15)
    try:
        uploads = paginator.page(page)
    except PageNotAnInteger:
        uploads = paginator.page(1)
    except EmptyPage:
        uploads = paginator.page(paginator.num_pages)
    return render(request, 'fips/file_list.html', {'categories': categories, 'uploads':uploads})

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

def handle_uploaded_file(file):
    if not os.path.exists('media/'):
        os.mkdir('media/')
    with open('media/' + str(file), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

@login_required
def add_image_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        print(request.FILES)
        form = ImageCommentForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['image'])
            image = form.save(commit=False)
            image.post = post
            image.author = request.user
            image.published_date = timezone.now()
            image.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ImageCommentForm()
    return render(request, 'fips/add_image_comment.html', {'form': form})

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

@login_required
def image_comment_approve(request, pk):
    image_comment = get_object_or_404(ImageComment, pk=pk)
    image_comment.approve()
    return redirect('post_detail', pk=image_comment.post.pk)

@login_required
def image_comment_remove(request, pk):
    image_comment = get_object_or_404(ImageComment, pk=pk)
    post_pk = image_comment.post.pk
    image_comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def upload_detail(request, pk):
    categories = Category.objects.filter().order_by('pk')
    upload = get_object_or_404(UploadFile, pk=pk)
    if upload.author != request.user:
        UploadFile.objects.filter(id=pk).update(hits=F('hits')+1)
    return render(request, 'fips/upload_detail.html', {'categories': categories, 'upload': upload})

@login_required
def upload_new(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['upload_file'])
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.author = request.user
            upload.published_date = timezone.now()
            upload.save()
            return redirect('upload_detail', pk=upload.pk)
    else:
        form = UploadFileForm()
    return render(request, 'fips/upload_edit.html', {'form': form})

@login_required
def upload_edit(request, pk):
    upload = get_object_or_404(UploadFile, pk=pk)
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['upload_file'])
        form = UploadFileForm(request.POST, request.FILES, instance=upload)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.author = request.user
            upload.published_date = timezone.now()
            upload.save()
            return redirect('upload_detail', pk=upload.pk)
    else:
        form = UploadFileForm(instance=upload)
    return render(request, 'fips/upload_edit.html', {'form': form})

@login_required
def upload_remove(request, pk):
    upload = get_object_or_404(UploadFile, pk=pk)
    upload.delete()
    return redirect('file-board')