from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from posts.models import Post

# Create your views here.
class ProfileUser(CreateView):
    
    template_name = 'profile_user.html'
    queryset = Post.objects.all()
    fields = '__all__'
    def get_context_data(self,**kwargs: Any) -> dict[str, Any]:
        user = User.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['user'] =  user 
        context['posts'] = Post.objects.filter(user=user)
        return context
    
