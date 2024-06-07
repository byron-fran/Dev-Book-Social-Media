from django.conf import settings
from django.shortcuts import redirect, render
from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def home(request):

    context = {'posts' : Post.objects.list_posts()}
    return render(request, 'home.html', context)