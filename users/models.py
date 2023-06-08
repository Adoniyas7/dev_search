from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
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
        return self.name