from django.shortcuts import render
from .models import Profile

# Create your views here.

def profiles(request):
    profile = Profile.objects.all()
    context = {"profiles": profile}
    return render(request, "users/profiles.html", context)