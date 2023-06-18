from django.db.models import Q
from.models import Project, Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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

def paginate_projects(request, projects, results):

    page = request.GET.get('page')
    result = results
    paginator = Paginator(projects, result)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    left = (int(page) - 4)

    if left < 1:
        left = 1

    right = (int(page) + 5)

    if right > paginator.num_pages:
        right = paginator.num_pages + 1

    custom_range = range(left, right)

    return custom_range, projects, paginator

                                          