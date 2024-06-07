from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    
    path('profile/<str:pk>/',views.ProfileUser.as_view(), name='profile' ),
    path('add/follow/<str:id_user>/', views.add_follow, name='add_follow'),
    path('remove/follow/<str:id_user>/', views.remove_follow, name='remove_follow'),
    # authentications
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
    
]
