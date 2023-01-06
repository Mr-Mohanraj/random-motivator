from django.db import models
from django.contrib.auth.models import AbstractBaseUser
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True,null=False)
    username = models.CharField(
        max_length=200, unique=True, null=False, default="newuser")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()


class Reset(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
