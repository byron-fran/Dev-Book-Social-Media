from django.urls import path
from . import views
urlpatterns = [
    path('profile/<str:pk>/',views.ProfileUser.as_view(), name='profile' )
]
