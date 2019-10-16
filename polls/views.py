from django.shortcuts import render

from django.http import HttpResponse

from .models import Posts


def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def post(request):
    posts  = Posts.objects.all() 
    return render(request, "post.html",{'posts':posts})    