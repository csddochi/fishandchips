from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.
def introduction(request):
    return render(request, 'fips/introduction.html', {})

def sign_in(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(request.POST)
    user = authenticate(username=username, password=password)
    print('result:', user)
    if user is not None:
        login(request, user)
        return render(request, 'fips/main.html', {})
    else: # create a user account
        return sign_up(request, username, password)

def sign_up(request, username, password):
    email = request.POST.get('email')
    _referrer = request.POST.get('referrer')
    print('email:', email, '/ referrer:', _referrer)
    if email is not None and _referrer is not None:
        _password = make_password(password)
        _user = User(username=username, email=email, password=_password)
        _user.referrer = _referrer
        print('ref_code:', _user.ref_code)
        _user.save()
        return render(request, 'registration/sign-up.html', {})
    else:
        return render(request, 'registration/login.html', {})

def logout(request):
    return render(request, 'fips/introduction.html', {})

@login_required
def main(request):
    return render(request, 'fips/main.html', {})
