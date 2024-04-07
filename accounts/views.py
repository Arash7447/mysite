from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from accounts.backends import EmailOrUsernameModelBackend
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def login_view(request) :
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        user = EmailOrUsernameModelBackend().authenticate(request, username=username_or_email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
    return render(request, 'accounts/login.html')


def logout_view(request) :
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def signup_view(request) :
    if not request.user.is_authenticated:
        if request.method == 'POST' :
            form = UserCreationForm(request.POST)
            if form.is_valid() :
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {'form': form}
        return render(request,'accounts/signup.html', context)
    else:
        return redirect('/')