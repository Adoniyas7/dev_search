from django.shortcuts import render, redirect
from .models import Project, Tag, Review
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .utils import search_project, paginate_projects

# Create your views here.

def home(request):
    return render(request, "index.html")

def projects(request):
    project_query, projects = search_project(request)
    custom_range, projects, paginator = paginate_projects(request, projects, 3)  
                      
    context = {"projects": projects, "project_query": project_query, "paginator": paginator, "custom_range": custom_range}
    return render(request, "projects/projects.html", context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, "projects/single-project.html", context)

@login_required(login_url='login')
def add_project(request):
    profile = request.user.profile
    form = ProjectForm()
    context = {"form": form}

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
          project = form.save(commit=False)
          project.owner= profile
        
          project.save()
          messages.success(request, "Project added successfully")

          return redirect("projects")

    return render(request, 'projects/add-project.html', context)

@login_required(login_url='login')
def edit_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance = project)
    context = {"form": form}

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
          form.save()
          messages.success(request, "Project edited successfully")
          return redirect("projects")

    return render(request, 'projects/add-project.html', context)

@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {"object":project}
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully")
        return redirect("projects")

        
    return render(request, "delete.html", context)