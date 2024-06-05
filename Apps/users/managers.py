from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager, models.Manager):

    def _create_user(
        self, email, password, is_staff : bool, is_superuser : bool, is_active : bool, **kwargs
    ):
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email, password, True, True, True, **kwargs)

    def create_user(self, username, password, **kwargs):
        return self._create_user(username, password, False, False, False, **kwargs)