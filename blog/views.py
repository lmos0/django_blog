from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/posts.html')

def single_post(request):
    return render(request, 'blog/single_post.html')