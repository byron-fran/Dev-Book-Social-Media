from django.contrib import admin
from .models import User, Follows
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass

class FollowsAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Follows, FollowsAdmin)
