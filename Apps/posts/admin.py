from django.contrib import admin
from .models import Post, Like,Saved

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

class LikeAdmin(admin.ModelAdmin):
    pass

class SavedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Saved, SavedAdmin)