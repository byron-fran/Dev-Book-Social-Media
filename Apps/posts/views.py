from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from .models import Post, Like, Saved
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from comments.models import Comment
from comments.forms import CommentForm

# Create your views here.

class ListPosts(LoginRequiredMixin,  ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name =  'posts'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)    
        context['posts'] = Post.objects.list_post()
        return context
    
    
def add_like(request : HttpRequest, pk : str, path ):
    post = Post.objects.get(id=pk)
  
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

class ListLikes(LoginRequiredMixin,ListView):
    
    model = Post
    template_name = 'likes.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)  
        likes = []  
        likes_mapper = self.request.user.likes.all()
        
        for lm in likes_mapper:
            likes.append(lm.post)
  
        context['posts'] = likes
        return context
    
# saved posts

def add_saved(request: HttpRequest, pk : str, path : str):
    
    post = Post.objects.get(id=pk)
    try:
        new_saved = Saved(post=post,user=request.user)
        new_saved.save()
    except post.DoesNotExist:
        raise Exception('error')
    
    return redirect(path)

def remove_saved(request : HttpRequest, pk : str, path : str):
    post = Post.objects.get(id=pk)
    try:
        saved = Saved.objects.filter(post=post, user=request.user)
        saved.delete()
        
    except post.DoesNotExist:
        raise Exception("error")
    
    return redirect(path)


class ListSavedPosts(LoginRequiredMixin, ListView):
    
    model = Post
    template_name = 'saved.html'    
    
    def  get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        saved = []
        saved_mapper =self.request.user.saved.all()
        
        for sm  in saved_mapper:
            saved.append(sm.post)
        context['posts'] =  saved    
        return context
       
class UpdatePost(LoginRequiredMixin,  UpdateView):
    model = Post
    fields = ['content', 'image', 'published']
    template_name = 'update_post.html'
    
    def get_success_url(self) -> str:
        id = self.kwargs['pk']
        self.success_url = f'/posts/update_post/{id}/?ok=1'
        return super().get_success_url()
    
    
def delete_post(request : HttpRequest,pk : str, path : str):
    post = Post.objects.get(id=pk, user=request.user)
    try:
        post.delete()
    except post.DoesNotExist:
        raise Exception('erro delete')
    return redirect(path) 

class DetailPost(DetailView):
    
    model = Post
    template_name ='detail.html'
    context_object_name = 'post'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        context['comments'] = comments
        context['form'] = CommentForm()
        context['id'] = post.pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user  # Asegúrate de que el usuario esté autenticado
            comment.save()
            return redirect(reverse('posts:detail', kwargs={'pk': self.object.pk}))
        return self.get(request, *args, **kwargs)
  
