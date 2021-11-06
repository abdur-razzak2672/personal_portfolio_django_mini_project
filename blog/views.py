from django.shortcuts import render
from .models import blog

def all_blogs(request):

    blogs = blog.objects.all()
    return render(request , 'blog/all_blogs.html',{'blogs':blogs})
    
