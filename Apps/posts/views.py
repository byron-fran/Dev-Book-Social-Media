from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.


class ListPosts(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name =  'posts'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)    
        context['posts'] = Post.objects.list_post()
        return context