from django.shortcuts import render, redirect
from django.http import HttpResponse

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def menu(request):
    return render(request, 'menu.html')