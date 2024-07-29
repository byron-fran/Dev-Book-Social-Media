from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_filter =[ 'user', 'post']
    search_fields = ['user', 'content', 'post']
    

admin.site.register(Comment, CommentAdmin)