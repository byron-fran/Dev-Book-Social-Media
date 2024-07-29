from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
  
    class Meta:
        model = Comment
        fields =['comment']
        widgets = {
        'comment': forms.Textarea(attrs={
            'class': 'w-full mx-auto  col-span-11 border border-slate-300 rounded-md block  bg-transparent resize-none focus:outline-none h-[50px]', 'placeholder' : 'reply'}),
          
        }