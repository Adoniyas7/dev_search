
from django.db.models import Q
from .models import Profile, Skill
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search_profile(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    skill = Skill.objects.filter(name__icontains=search_query)
    profile = Profile.objects.distinct().filter(Q(name__icontains=search_query) |
                                    Q(short_intro__icontains=search_query) |
                                    Q(skill__in= skill)
                                    )
    return profile, search_query

def paginate_profiles(request, profiles, result):
    
    page = request.GET.get('page')
    profiles = profiles
    paginator = Paginator(profiles, result)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left = (int(page) - 4)

    if left < 1:
        left = 1

    right = (int(page) + 5)

    if right > paginator.num_pages:
        right = paginator.num_pages + 1

    custom_range = range(left, right)

    return custom_range, profiles
