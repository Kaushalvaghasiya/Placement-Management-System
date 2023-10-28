# views.py

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import StudentSignUpForm, HeadSignUpForm
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, EmployerProfile, HeadProfile


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            full_name = user.full_name
            profile = StudentProfile(user=user,full_name=full_name)
            profile.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        form = StudentSignUpForm()
    return render(request, 'student_signup.html', {'form': form})

def head_signup(request):
    if request.method == 'POST':
        form = HeadSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            full_name = user.full_name
            profile = HeadProfile(user=user,full_name=full_name)
            profile.save()
            login(request, user)
            return redirect('head_dashboard')
    else:
        form = HeadSignUpForm()
    return render(request, 'head_signup.html', {'form': form})

def employer_signup(request):
    if request.method == 'POST':
        form = HeadSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            full_name = user.full_name
            profile = EmployerProfile(user=user,company_name=full_name)
            profile.save()
            login(request, user)
            return redirect('employer_dashboard')
    else:
        form = HeadSignUpForm()
    return render(request, 'employer_signup.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password, type="student")
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            print(username, password)
    return render(request, 'student_login.html')

def head_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password, type="head")
        if user is not None:
            login(request, user)
            return redirect('head_dashboard')
        else:
            print(username, password)
    return render(request, 'head_login.html')

def employer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password, type="employer")
        if user is not None:
            login(request, user)
            return redirect('employer_dashboard')
        else:
            print(username, password)
    return render(request, 'employer_login.html')

@login_required(login_url='student_login')
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required(login_url='head_login')
def head_dashboard(request):
    return render(request, 'head_dashboard.html')

@login_required(login_url='employer_login')
def employer_dashboard(request):
    return render(request, 'employer_dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('student_login')
