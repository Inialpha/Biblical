""" This module contains code for the user model """
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from authemail.models import EmailUserManager, EmailAbstractUser


class User(EmailAbstractUser, PermissionsMixin):
    """ A user class email functionalities """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField()
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = EmailUserManager()

    def has_perms(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        # Assume all users have permissions to all modules for simplicity
        return True
