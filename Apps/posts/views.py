from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Post, Like
from django.http import HttpRequest, HttpResponse

# Create your views here.

class ListPosts(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name =  'posts'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)    
        context['posts'] = Post.objects.list_post()
        return context
    
    
def add_like(request : HttpRequest, pk : str,path ):
    post = Post.objects.get(id=pk)
    print(path, 'path')
    try:
        new_like = Like(user=request.user, post=post)
        new_like.save()
    
    except post.DoesNotExist:
        
        raise Exception('error to like')
    
    return redirect(path)


def remove_like(request : HttpRequest, pk : str, path : str):
    post = Post.objects.get(id=pk)
  
    try:
        like =  Like.objects.filter(post=post, user=request.user)
        like.delete()
        
    except post.DoesNotExist:
        pass
    return redirect(path)