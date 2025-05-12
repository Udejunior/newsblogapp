from django.shortcuts import render
from .models import Blog_Post

# Create your views here.
def index(request):
    full_post = Blog_Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'full_post': full_post})

def news(request):
    full_post = Blog_Post.objects.all().order_by('-created_at')
    return render(request, 'news.html', {'full_post': full_post})

def business(request):
    full_post = Blog_Post.objects.all().order_by('-created_at')
    return render(request, 'business.html', {'full_post': full_post})

def politics(request):
    full_post = Blog_Post.objects.all().order_by('-created_at')
    return render(request, 'politics.html', {'full_post': full_post})

def sport(request):
    full_post = Blog_Post.objects.all().order_by('-created_at')
    return render(request, 'sport.html', {'full_post': full_post})

def entertainment(request):
    full_post = Blog_Post.objects.all().order_by('-created_at')
    return render(request, 'entertainment.html', {'full_post': full_post})

def others(request):
    full_post = Blog_Post.objects.all().order_by('-created_at')
    return render(request, 'others.html', {'full_post': full_post})

