from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager, models.Manager):

    def _create_user(
        self, username,email, password, is_staff : bool, is_superuser : bool, is_active : bool, **kwargs
    ):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            username=username,
            **kwargs
        )
        user.set_password(password)  # Asegúrate de que esto esté correctamente configurado
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **kwargs):
        return self._create_user(username,email, password, True, True, True, **kwargs)

    def create_user(self, username,email, password, **kwargs):
        return self._create_user(username,email, password, False, False, False, **kwargs)