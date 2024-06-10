from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView, ListView
from django.views.generic.edit import UpdateView
from .models import User
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from .models import Follows
from django.db import IntegrityError
from .forms import RegisterForm, LoginForm,ChangePasswordForm
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

#followers
class Followers(LoginRequiredMixin,ListView):
    model = Follows
    context_object_name = 'followers'
    template_name = 'follows/followers.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        id = self.kwargs['pk']
        user = User.objects.get(id=id)
        followers  = Follows.objects.filter(follower=user)
        context['followers'] =  followers
    
        return context
    
    
class Followings(LoginRequiredMixin, ListView):
    model = Follows
    context_object_name = 'followings'
    template_name = 'follows/followings.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      
        context = super().get_context_data(**kwargs) 
        id = self.kwargs['pk']
        user = User.objects.get(id=id)
        
        followings  = Follows.objects.filter(followed=user)
        context['followings'] =  followings
    
        return context 

    
# authentications
class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    
    success_url= reverse_lazy('home')
    
    def form_valid(self, form: Any) -> HttpResponse:
       
        user = form.save()
        
        if user is not None:
            user.backend = 'users.backends.EmailBackend'
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    

class LoginView( FormView):
    
    form_class = LoginForm
    template_name = 'auth/login.html'
   
    success_url = reverse_lazy('home')   
    
    def form_valid(self, form: Any) -> HttpResponse:

        email  = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            user.backend = 'users.backends.EmailBackend'
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Email or password incorrect')
            
            return super().form_invalid(form)
        
 

# logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/login/')
    
# Update profile
class UpdateProfile(LoginRequiredMixin, UpdateView):
    
    model = User
    fields= ['username', 'email', 'bio', 'first_name', 'last_name', 'birthdate', 'photo_profile']
    template_name = 'profile/profile_update.html'
    
    def get_success_url(self) -> str:
        id = self.kwargs['pk'] 
        self.success_url = f'/update/{id}/?ok=1'
        return super().get_success_url()

    
# passwords
class ChangePassword(LoginRequiredMixin, FormView):
    template_name = 'passwords/change_password.html'
    form_class = ChangePasswordForm
    
    success_url = reverse_lazy('users:change_password')
    
    def form_valid(self, form):
        user = self.request.user
        password = self.request.POST.get('password')
        new_password = self.request.POST.get('new_password')
        new_password2 = self.request.POST.get('new_password2')
        
        if user.check_password(password):
            
            if new_password != new_password2:
                
                messages.error(self.request, 'password must match')
                return super().form_invalid(form)
            
            messages.success(self.request, 'password change success')
            user.set_password(new_password)
            user.save()
              
            # Re-authenticate the user after changing the password
            update_session_auth_hash(self.request, user)  
            
            return super().form_valid(form)
        
        messages.error(self.request, 'Invalid password')
        return super().form_invalid(form)
            
    
    
