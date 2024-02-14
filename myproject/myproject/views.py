from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import (
    CustomUserCreationForm,
    AuthenticationForm,

)
from django.contrib import messages
from datetime import date




def homepage(request):

    return render (request, 'homepage.html')


def signupPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('signinPage')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signUP_page.html', {'form': form})

def signinPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('homepage')
    else:
        form = AuthenticationForm()

    return render(request, 'signin_page.html', {'form': form})

def logoutPage(request):
    logout(request)
    # Optionally, display a logout message
    messages.info(request, "You have been logged out successfully.")
    return redirect('signinPage')
