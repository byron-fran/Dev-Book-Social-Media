from typing import Any
from django import forms
from .models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    
    email = forms.EmailField(
        label='Email', 
        required=True, 
        # error_messages='email is required', 
        max_length=200, 
        widget=forms.TextInput(attrs={'class' : 'w-full border-none rounded-md p-2 my-2 '}))
    
    password = forms.CharField(
        min_length=8, 
        max_length=200,
        # error_messages='password is required',
        widget=forms.PasswordInput( attrs={'class' : 'w-full border-none rounded-md p-2 my-2 ',  'autocomplete':"on"}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password")
        
        return cleaned_data

class RegisterForm(forms.ModelForm):
    
    email = forms.EmailField(
        label='', 
        help_text='email',
        required=True, 
        max_length=200, 
        widget=forms.EmailInput(attrs={'class' : 'w-full border-none rounded-md p-2 my-2 '}))

    username = forms.CharField(
        label='',
        help_text='username',
        min_length=2, 
        max_length=200,
        widget=forms.TextInput(attrs={'class' : 'w-full border-none rounded-md p-2 my-2 '}))
    
    password = forms.CharField(
        label='',
        help_text='password',
        min_length=8, 
        max_length=200,
        widget=forms.PasswordInput( attrs={'class' : 'w-full border-none rounded-md p-2 my-2 ',  'autocomplete':"on"}))
    
    password2 = forms.CharField(
        help_text='repeat your password',
        label='',
        min_length=8, 
        max_length=200,
        widget=forms.PasswordInput( attrs={'class' : 'w-full border-none rounded-md p-2 my-2 ',  'autocomplete':"on"}))
    
    class Meta:
        model = User 
        fields = ['email', 'username','password']    
        
    
    def clean_password2(self) -> dict[str, Any]:
        
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
    
            self.add_error('password2', 'password do not match')
            
    def clean_email(self)  -> dict[str, Any]:
        
        email = User.objects.filter(email=self.cleaned_data['email'])
        
        if email.exists():
       
          return  self.add_error('email', 'email already exists')
          
        return self.cleaned_data['email']
    
    def clean_username(self) -> dict[str, Any]:
 
        username = User.objects.filter(username=self.cleaned_data['username'])
        if username.exists():
            return self.add_error('username', 'username already exists')
  
        return self.cleaned_data['username']
    
    def save(self, commit: bool = ...) -> Any:
        password = self.cleaned_data['password']
        self.instance.set_password(password)
        return super().save(commit)
    
        