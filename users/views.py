from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def profiles(request):
    profile = Profile.objects.all()
    context = {"profiles": profile}
    return render(request, "users/profiles.html", context)

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    context = {"profile": profile, "top_skills":top_skills, "other_skills": other_skills}
    return render(request, "users/user-profile.html", context)

def login_users(request):

    context = {"page":"login" }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try: 
            user = User.objects.get(username=username)
        except:
            print("there is no user name with the provided")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
            

    return render(request, "users/login.html", context)

def logout_user(request):
    logout(request)
    return render(request, "users/profiles.html")