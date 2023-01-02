from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100,unique=True,blank=False)
    password = models.CharField(max_length=32,blank=False)
    created_at = models.DateTimeField(blank=False,null=False,auto_now_add=True)
    modify_at  = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    name = models.CharField(max_length=100,blank=False, null= False)
    # description = models.TextField(max_length=1000, default="None")
    bio = models.TextField(max_length=1000,default="None")


