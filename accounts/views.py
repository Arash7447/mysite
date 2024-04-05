from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

# Create your views here.

def login_view(request) :
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
    return render(request, 'accounts/login.html')


def logout_view(request) :
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def signup_view(request) :
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('/')
    form = UserCreationForm ()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
