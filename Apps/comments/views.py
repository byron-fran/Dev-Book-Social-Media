from typing import Any
from django.shortcuts import render
from .models import Comment
from django.views.generic.list import ListView

# Create your views here.
class ListComments(ListView):
    model =  Comment
    template_name = 'comments.html'
    context_object_name = 'comments'
    # queryset = Comment.objects.all()
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['saludo'] = 'Hola mundo'
        return context 