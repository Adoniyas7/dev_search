from django.shortcuts import render
from .models import Project, Tag, Review
from .forms import ProjectForm
# Create your views here.

def home(request):
    return render(request, "index.html")

def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, "projects/single-project.html", context)

def add_project(request):
    form = ProjectForm()
    context = {"form": form}
    return render(request, 'projects/add-project.html', context)