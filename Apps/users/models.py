from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from model_utils.models import TimeStampedModel
from .managers import UserManager
import uuid

# Create your models here.
class User (AbstractBaseUser,PermissionsMixin):
    
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    first_name=models.CharField(max_length=200)
    last_name = models.CharField(null=True, blank=True,max_length=200)
    
    # birthdate =models.DateField(null=True)
    
    photo_profile = models.ImageField(upload_to='profiles_photo/', null=True, blank=True)
    image_background = models.ImageField(upload_to='background/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    objects = UserManager()
    
    class Meta:
        
        db_table='users'
        verbose_name='user'
        verbose_name_plural='users'
    
    def __srt__(self):
        return self.username
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD ='email'
    
class Follows(TimeStampedModel):
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    
    class Meta:
        db_table= 'follows'
        verbose_name='follow'
        verbose_name_plural='follows'