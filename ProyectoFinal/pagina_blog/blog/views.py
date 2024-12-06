from django.shortcuts import render, get_object_or_404
from .models import Blog

def about(request):
    return render(request, 'blog/about.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, page_id):
    blog = get_object_or_404(Blog, id=page_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})
