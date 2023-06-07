from django.db import models
from uuid import uuid4

# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default = uuid4, unique=True, primary_key=True, editable=False)
    # owner = models
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_img = models.ImageField(upload_to="project_img")
    demo_link = models.CharField(max_length=200, null= True, blank=True)
    source_link = models.CharField(max_length=200, null= True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    vote_count = models.IntegerField(default=0, null=True, blank=True)
    #tags = models
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


