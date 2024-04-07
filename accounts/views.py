from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from accounts.backends import EmailOrUsernameModelBackend
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)

from django.urls import reverse_lazy
from .forms import *
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']
        user = EmailOrUsernameModelBackend().authenticate(request, username=username_or_email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Your username or password is incorrect.')
    return render(request, 'accounts/login.html')


def logout_view(request) :
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
              form=SignUpForm(request.POST)
              if form.is_valid():
                form.save()
                return redirect('/')
        
        form=SignUpForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
          return redirect('/')
    
# classes are for reset password section:

class PasswordReset(PasswordResetView):
    template_name="registration/password_reset_form.html"
    success_url=reverse_lazy("registration:password_reset_done")

class PasswordResetDone(PasswordResetDoneView):
    template_name="registration/password_reset_done.html"
    success_url=reverse_lazy("registration:password_reset_confirm")

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name="registration/password_reset_confirm.html"
    success_url=reverse_lazy("registration:password_reset_complete")

class PasswordResetComplete(PasswordResetCompleteView):
    template_name="registration/password_reset_complete.html"