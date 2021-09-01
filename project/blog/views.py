from django.shortcuts import render

# Create your views here.

def index(request):
    pass

def posts (request):
    return render(request , 'blog/posts.html')

def post_detail (request , slug):
    return render(request , 'blog/post-detail.html')
