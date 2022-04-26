from django.shortcuts import render, redirect
from .models import *
# from .forms import *
from django.contrib import messages

def home(request):
    return render(request, 'home.html',{})