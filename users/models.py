from django.db import models

from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , null=True, blank=True )
    name= models.CharField(max_length=200,null=True, blank=True)
    email=models.EmailField(max_length=500,null=True, blank=True)
    userName= models.CharField(max_length=200,null=True, blank=True)
    location= models.CharField(max_length=200,null=True, blank=True)
    short_intro=models.TextField(max_length=200,null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    profile_image=models.ImageField(upload_to='profiles/',null=True, blank=True, default='profiles/user-default.png')
    social_github= models.CharField(max_length=200,null=True, blank=True)
    social_twitter= models.CharField(max_length=200,null=True, blank=True)
    social_linkedin= models.CharField(max_length=200,null=True, blank=True)
    social_youtube= models.CharField(max_length=200,null=True, blank=True)
    social_website= models.CharField(max_length=200,null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return  str(self.user.username)

class skills(models.Model):
    owner=models.ForeignKey(profile,on_delete=models.CASCADE,null=True, blank=True) 
    name= models.CharField(max_length=200,null=True, blank=True) 
    description=models.TextField(null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self):
        return self.name     


class message (models.Model):
    sender = models.ForeignKey(profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient=models.ForeignKey(profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    name= models.CharField(max_length=200,null=True, blank=True)
    email= models.EmailField(max_length=200,null=True, blank=True)
    subject=models.CharField(max_length=200,null=True, blank=True)
    is_read = models.BooleanField(default=False,null=True)
    body = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.subject

    class Meta :
        ordering = ['is_read' , '-created']    
