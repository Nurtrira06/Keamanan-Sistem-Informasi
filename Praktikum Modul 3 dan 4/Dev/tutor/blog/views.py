from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'Judul' : 'AppBlog',
        'h1' : 'Django',
        'menu' : [['/', 'Home'], ['/blog/recent', 'Recent'], ['/blog/post', 'Post']]
    }
    return render(request,'blog/index.html', context)

def recent(request):
    return HttpResponse("<h1>RECENT BLOG</h1>")

def post(request):
    return HttpResponse("<h1>INI ISINYA POST</h1>")

####
# def index(request):
#     context = {
#         'Judul' : 'blog1',
#         'h1' : 'Django'
#     }
#     return render(request,'blog/index.html', context)

# def recent(request):
#     context = {
#         'Judul' : 'blog2',
#         'h1' : 'Python'
#     }
#     return render(request,'blog/index.html', context)

####
# def index(request):
#     return render(request,'blog/index.html')

# def recent(request):
#     return HttpResponse('RECENT')

# def index(request):
#     return HttpResponse("Ini Index")



# def about(request):
#     return HttpResponse("Ini About")