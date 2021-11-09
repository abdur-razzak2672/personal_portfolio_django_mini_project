from django.shortcuts import render , get_object_or_404
from .models import blog

def all_blogs(request):

    blogs = blog.objects.order_by('-date')
    return render(request , 'blog/all_blogs.html',{'blogs':blogs})


def blog_detail(request, blog_id) :
    all_blog = get_object_or_404(blog , pk=blog_id)
    return render(request,'blog/blog_details.html',{'all_blog':all_blog})
