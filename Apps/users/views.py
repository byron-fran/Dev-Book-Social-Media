from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Follows
from django.db import IntegrityError

# Create your views here.
class ProfileUser(LoginRequiredMixin, CreateView):
    
    template_name = 'profile_user.html'
    queryset = Post.objects.all()
    fields = '__all__'
    login_url = 'home'
    
    def get_context_data(self,**kwargs: Any) -> dict[str, Any]:
        user = User.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['user'] =  user 
        context['posts'] = Post.objects.filter(user=user)
        context['followers'] = user.followers.all().count()
        context['following'] = user.following.all().count()
        try:
            is_follow = self.request.user.following.filter(follower=user)
            if is_follow:
                context['is_following'] = True
            else:
                context['is_following'] = False
        except:
            pass
        return context
    

def add_follow(request, id_user):

    try:
        user = User.objects.get(id=id_user)
        user_local = request.user
        
        Follows.objects.create(
            followed=user_local,
            follower=user
        )
        
    except IntegrityError:
        pass
    
    
    return redirect('users:profile', id_user)

def remove_follow(request, id_user):
    
    user = User.objects.get(id=id_user)
    user_local = request.user
    
    try:
        # Buscar la relación de seguimiento
        follow_instance = Follows.objects.filter(follower=user, followed=user_local)
        follow_instance.delete()
    except IntegrityError:
        pass
    
    except user.DoesNotExist:
        pass
    
    return redirect('users:profile', id_user)
