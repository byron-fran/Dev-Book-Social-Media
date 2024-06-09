from django.urls import path
from . import views
app_name='posts'

urlpatterns = [
    
    path('add_like/<str:pk>/<path:path>/', views.add_like, name='add_like'),
    path('remove_like/<str:pk>/<path:path>/', views.remove_like, name='remove_like')
]
