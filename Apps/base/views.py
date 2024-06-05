from django.shortcuts import render
from django.shortcuts import render
from posts.models import Post
# Create your views here.
def home(request):
    
    context = {
        'posts' : Post.objects.list_posts()
    }
    return render(request, 'home.html', context)