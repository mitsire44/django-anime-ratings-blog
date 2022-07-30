from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def blogs(request):
    blog = Blog.objects.all()
    return render(request, 'blog/index.html', {'blogs':blog})


def fullblog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/fullblog.html', {'blog':blog})
