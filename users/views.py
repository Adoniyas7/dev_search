from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from django.contrib import messages

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

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist")
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error       (request, "Username or Password is incorrect")
            

    return render(request, "users/login.html", context)

def logout_user(request):
    logout(request)
    return redirect("profiles")

def register_user(request):
    form = UserRegistrationForm()
    context = {"page":"register", "form":form, "errors":[]}

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower().stripe()
            user.save()
            messages.success(request, "User Created sucessfully")

            return redirect("register")
        else:
            for field in form:
                for error in field.errors:
                    context['errors'].append(error)
            return render(request, "users/login.html", context)



    return render(request, "users/login.html", context)