from django.shortcuts import render, get_object_or_404
from .models import Blog

def index(request):
    recent_blogs = Blog.objects.order_by('-time_published')[:3]
    popular_blogs = Blog.objects.all()[:6]
    blog = get_object_or_404(Blog, id=1)
    return render(request, 'main/index.html', {'recent_blogs': recent_blogs, 'popular_blogs': popular_blogs, 'blog': blog})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/blog_detail.html', {'blog': blog})

def all_blogs(request):
    all_blogs = Blog.objects.all()
    return render(request, 'main/all_blogs.html', {'all_blogs': all_blogs})

def single_blog(request):
    blog = get_object_or_404(Blog, id=1)
    return render(request, 'main/single_blog.html', {'blog': blog})

def blog(request):
    return render(request, 'main/blog.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def search(request):
    return render(request, 'main/search.html')

def custom_404(request, exception):
    return render(request, 'main/404error.html')