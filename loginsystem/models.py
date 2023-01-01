from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=16,blank=False)
    created_at = models.DateTimeField(blank=False,null=False,auto_now_add=True)
    modify_at  = models.DateTimeField(blank=False, null=False, auto_now_add=True)
