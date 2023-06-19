from django.db import models
from uuid import uuid4
from users.models import Profile

# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default = uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null= True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_img = models.ImageField(upload_to="project_img")
    demo_link = models.CharField(max_length=200, null= True, blank=True)
    source_link = models.CharField(max_length=200, null= True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    vote_count = models.IntegerField(default=0, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-vote_ratio', '-vote_count', 'title']

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVote = reviews.filter(value="up").count()
        totalVote = reviews.count()
        ratio = (upVote/totalVote) * 100
        self.vote_count = totalVote
        self.vote_ratio = ratio
        self.save()
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset


    
class Tag(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Review(models.Model):
    VOTE_TYPE = (
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self) -> str:
        return self.value
    
    # def getVoteCount(self):
    #     reviews = self.review_set.all()
    #     upVote = reviews.filter(value="up").count()
    #     totalVote = reviews.count()
    #     ratio = (upVote/totalVote) * 100
    #     self.project.vote_count = totalVote
    #     self.project.vote_ratio = ratio
    #     self.project.save()
    #     self.save()


