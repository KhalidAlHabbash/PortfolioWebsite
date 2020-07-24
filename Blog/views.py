from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    all_blogs = Blog.objects
    return render(request,'Blog/allblogs.html',{'all_blogs':all_blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request,'Blog/detail.html', {'detailblog':blog_detail})

