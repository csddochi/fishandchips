from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.
def introduction(request):
    return render(request, 'fips/introduction.html', {})

def sign_in(request):
    username = request.POST.get('username', '')
    print('username:', username)
    password = request.POST.get('password', '')
    print('password:', password)
    print(request.POST)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'fips/main.html', {})
    else: # create a user account
        email = request.POST.get('email')
        print('email:', email)
        _referrer = request.POST.get('referrer')
        print('referrer:', _referrer)
        if email is not None and _referrer is not None:
            _user = User(username=username, email=email, password=password)
            _user.referrer = _referrer
            _user.save()
            return render(request, 'registration/sign-up.html', {})
        else:
            return render(request, 'registration/login.html', {})

def logout(request):
    return render(request, 'fips/introduction.html', {})

def main(request):
    return render(request, 'fips/main.html', {})
