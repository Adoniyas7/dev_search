from django.shortcuts import render, redirect
from .models import Profile, Skill
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, ProfileForm, SkillForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import search_profile



# Create your views here.

def profiles(request):
    profiles, search_query = search_profile(request)
   
    context = {"profiles": profiles, "search_query":search_query}
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
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User Created sucessfully")

            login(request, user)
            return redirect("profiles")
        else:
            for field in form:
                for error in field.errors:
                    context['errors'].append(error)
            return render(request, "users/login.html", context)



    return render(request, "users/login.html", context)

@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {"profile": profile, "skills":skills, "projects": projects}
    return render(request, "users/account.html", context)

def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    context = {"form":form}

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Edited successfully")
            return redirect('user-account')
        else:
            messages.error(request, "Error happend while editing the profile")
            return redirect('edit-account')

    return render(request, 'users/profile-form.html', context)

@login_required(login_url="login")
def add_skill(request):
    profile = request.user.profile
    form = SkillForm()
    context = {"form":form}

    if request.method == 'POST':
        print("Post")
        form = SkillForm(request.POST)
        if form.is_valid():
            print("validddd")
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill added sucessfully")
            return redirect('user-account')
        
    return render(request, 'users/skill-form.html', context)

@login_required(login_url="login")
def edit_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    context = {"form":form}
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill updated sucessfully")
            return redirect('user-account')
        
    return render(request, 'users/skill-form.html', context)

def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    context = {"object":skill}

    if request.method == 'POST':
        skill.delete()
        messages.success(request, "Skill deleted successfully")
        return redirect('user-account')

    return render(request, 'delete.html', context)