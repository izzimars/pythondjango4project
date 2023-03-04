from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    all_b = Blog.objects.all()
    return render(request,"blog/all_blogs.html",{"blogs":all_b})


def details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,"blog/detail.html",{"blog":blog})
