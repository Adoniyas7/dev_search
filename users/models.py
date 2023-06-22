from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_pic =models.ImageField(upload_to="profile_pic/", default="profile_pic/default.png")
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.username)

class Skill(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_id = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Message(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False )
    sender = models.ForeignKey(Profile, on_delete= models.SET_NULL, null = True,  blank=True)
    recipiebt = models.ForeignKey(Profile, on_delete= models.SET_NULL, null = True,  blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null= True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ['is_read', '-created_at']
