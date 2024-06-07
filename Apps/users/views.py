from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView
from .models import User
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from .models import Follows
from django.db import IntegrityError
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

class ProfileUser(LoginRequiredMixin, CreateView):
    
    template_name = 'profile/profile_user.html'
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

# authentications
class LoginView( FormView):
    
    form_class = LoginForm
    template_name = 'auth/login.html'
   
    success_url = reverse_lazy('home')   
    
    def form_valid(self, form: Any) -> HttpResponse:

        email  = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Email or password incorrect')
            return super().form_invalid(form)
        
 

# logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(
        redirect_to='/login/'
    )