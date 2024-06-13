from django.conf import settings
from django.shortcuts import redirect, render
from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm
from django.http import HttpRequest
# Create your views here.

@login_required
def home(request : HttpRequest):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')  
    else:
        form = PostForm()
            
    
    context = {'posts' : Post.objects.list_posts(), 'form' : form}
    return render(request, 'home.html', context)

@login_required    
def settings(request : HttpRequest):
    
    return render(request, 'settings.html')  
    