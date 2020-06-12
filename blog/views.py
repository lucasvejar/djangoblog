from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Post


def index(request):
    return HttpResponse("Hello dear web page")

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) 

def post_detail(request, pk):
    post = Post.objects.get(id=pk) #get_object_or_404(request, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})