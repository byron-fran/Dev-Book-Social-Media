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
    
    class Meta:
        model = User 
        fields = ['password', 'email', 'username']    
    def clean_email(self) -> dict[str, Any]:
        return