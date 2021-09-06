from django.shortcuts import render

# Create your views here.

all_posts = [
    {'title' : 'django course',
     'slug' : 'learning-django',
     'image': 'django.png',
     'content' :'contentcontentcontentcontentcontentcontentcontent',
     'summary' : 'summarysummarysummarysummarysummarysummarysummary'
    },
    {'title' : 'learning php',
     'slug' : 'learning-php',
     'image': 'python.png',
     'content' :'contentcontentcontentcontentcontentcontentcontent',
     'summary' : 'summarysummarysummarysummarysummarysummarysummary'
    },
    {'title' : 'learning git',
     'slug' : 'learning-git' , 
     'image': 'ml.png',
     'content' :'contentcontentcontentcontentcontentcontentcontent',
     'summary' : 'summarysummarysummarysummarysummarysummarysummary'
    }
]




def index(request):
    pass

def posts (request):
    return render(request , 'blog/posts.html' , {'posts' : all_posts})

def post_detail (request , slug):
    return render(request , 'blog/post-detail.html' )
