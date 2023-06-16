from django.db.models import Q
from.models import Project, Tag

def search_project(request):
    project_query = ''
    if request.GET.get('project_query'):
        project_query = request.GET.get('project_query')
    tags = Tag.objects.filter(name__icontains=project_query)
    projects = Project.objects.distinct().filter(Q(title__icontains=project_query) |
                                      Q(description__icontains=project_query) |
                                      Q(owner__name__icontains=project_query) |
                                      Q(tags__in=tags)
                                      )

    return project_query, projects
                                          