from django.shortcuts import render
from .models import Blog

def blogpage(request):
    all_blogs = Blog.objects
    return render(request,'Blog/blogpage.html', {'blogs':all_blogs})