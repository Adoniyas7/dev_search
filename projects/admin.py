from django.contrib import admin
from .models import Project, Tag, Review

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Review)
