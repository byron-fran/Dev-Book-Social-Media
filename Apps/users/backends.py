from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
import logging

User = get_user_model()
logger = logging.getLogger(__name__)

class EmailBackend(ModelBackend):
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('email')
        try:
            user = User.objects.get(email=username)

        except User.DoesNotExist:
     
            return None
        
        if user.check_password(password) :
            logger.info(f"Password check passed for user: {user.email}")
            return user
        else:
            logger.warning(f"Password check failed for user: {user.email}")
        return None