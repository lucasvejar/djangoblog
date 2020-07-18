from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post, Comment, User
from .forms import PostForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# flash messages
from django.contrib import messages





def registerUser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account created for '+user)
            return redirect('blog:login')

    context = {'form': form}
    return render(request,'blog/register.html',context=context)


def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('blog:post_list')
        else:
            messages.info(request,'Username OR password is incorrect')

    context = {}
    return render(request, 'blog/login.html',context=context)


def logoutUser(request):
    logout(request)
    return redirect('blog:login')



def post_list(request):
    posts = Post.objects.order_by('created_date')
    user = User.objects.get(pk=1)
    users = User.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'users': users, 'user': user}) 


def post_detail(request, pk):
    post = Post.objects.get(id=pk) #get_object_or_404(request, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request,'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})

