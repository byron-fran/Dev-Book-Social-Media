from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields =['comment']
        widgets = {
        'comment': forms.Textarea(attrs={'class': 'w-full border border-slate-300 resize-none focus:outline-none'}),
          
        }