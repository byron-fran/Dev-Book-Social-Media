from django.contrib import admin
from .models import Post, Like,Saved

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter =[ 'user', 'published']

class LikeAdmin(admin.ModelAdmin):
    list_filter =[ 'user', 'post']

class SavedAdmin(admin.ModelAdmin):
    list_filter =[ 'user', 'post']

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Saved, SavedAdmin)