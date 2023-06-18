
from django.db.models import Q
from .models import Profile, Skill


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

