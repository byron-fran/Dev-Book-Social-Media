from django.urls import path
from . import views

app_name='users'

urlpatterns = [
    
    path('profile/<str:pk>/',views.ProfileUser.as_view(), name='profile' ),
    path('add/follow/<str:id_user>/', views.add_follow, name='add_follow'),
    path('remove/follow/<str:id_user>/', views.remove_follow, name='remove_follow'),
    # authentications
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    # crud user
    path('update/<str:pk>/', views.UpdateProfile.as_view(), name='update'),
    path('delete_account/<str:pk>/', views.delete_account, name='delete_account'),
    # follows
    path('followers/<str:pk>/', views.Followers.as_view(), name='followers'),
    path('followings/<str:pk>/', views.Followings.as_view(), name='followings'),
    # password routes
    path('change_password/', views.ChangePassword.as_view(), name='change_password'),
    # search
    path('search/', views.ListSearchUsers.as_view(), name='search')
   
]
