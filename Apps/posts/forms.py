from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content' : forms.Textarea(attrs={'class': 'w-full border border-slate-300 resize-none focus:outline-none'}),
          
        }