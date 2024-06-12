from django.urls import path
from . import views
app_name='posts'

urlpatterns = [
    
    path('add_like/<str:pk>/<path:path>/', views.add_like, name='add_like'),
    path('remove_like/<str:pk>/<path:path>/', views.remove_like, name='remove_like'),
    path('likes/', views.ListLikes.as_view(), name='likes'),
    path('saved_add/<str:pk>/<path:path>/', views.add_saved, name='saved_add'),
    path('saved_remove/<str:pk>/<path:path>/', views.remove_saved, name='saved_remove'),
    path('saved/', views.ListSavedPosts.as_view(), name='saved_list'),
    # crud
    path('update_post/<str:pk>/', views.UpdatePost.as_view(), name='update_post'),
    path('delete_post/<str:pk>/<path:path>/', views.delete_post, name='delete_post')
]
