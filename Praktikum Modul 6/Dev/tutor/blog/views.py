from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    db = Post.objects.all()
    context ={
        'title':'Blog',
        'heading':'Blog',
        'subheading': 'postingan',
        'post' : db,
    }
    # context = {
    #     'Judul' : 'AppBlog',
    #     'h1' : 'Django',
    #     'menu' : [['/', 'Home'], ['/blog/recent', 'Recent'], ['/blog/post', 'Post']]
    # }
    return render(request,'blog/index.html', context)

def recent(request):
    return HttpResponse("<h1>RECENT BLOG</h1>")

def post(request):
    return HttpResponse("<h1>INI ISINYA POST</h1>")

