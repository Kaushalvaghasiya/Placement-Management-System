# views.py

from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import StudentSignUpForm, HeadSignUpForm, EmployerSignUpForm, StudentUpdateProfileForm, EmployerUpdateProfileForm
from django.contrib.auth.decorators import login_required
from .models import StudentProfile, EmployerProfile, HeadProfile
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from job_management.models import Job
from django.core.mail import send_mail

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Send a welcome email to the user
            subject = 'Welcome to Our Website'
            message = 'Thank you for registering!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            # Send the email
            send_mail(subject, message, from_email, recipient_list)
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
        form = EmployerSignUpForm(request.POST)
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

@login_required(login_url='student_login')
def student_update_profile(request):
    if request.method == 'POST':
        form = StudentUpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            resume = form.cleaned_data['resume']
            fullname = form.cleaned_data['full_name']
            dob = form.cleaned_data['date_of_birth']
            cno = form.cleaned_data['contact_number']
            address = form.cleaned_data['address']
            filename = f'student_{request.user.id}_resume.pdf'
            storage = FileSystemStorage(location=settings.MEDIA_ROOT / 'resumes')
            storage.save(filename, resume)
            obj = StudentProfile.objects.get(user_id=request.user)
            obj.full_name=fullname
            obj.date_of_birth=dob
            obj.contact_number=cno
            obj.address=address
            obj.resume=filename
            obj.save()
            return redirect('student_profile')
    else:
        user = StudentProfile.objects.get(user_id=request.user)
        form = StudentUpdateProfileForm(instance=user)
    return render(request, 'student_profile_update.html', {'form': form})

@login_required(login_url='student_login')
def student_profile(request):
    profile = StudentProfile.objects.get(user_id=request.user)
    return render(request, 'student_profile.html', {'profile': profile})

@login_required(login_url='employer_login')
def employer_update_profile(request):
    if request.method == 'POST':
        form = EmployerUpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data['company_name']
            industry = form.cleaned_data['industry']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            obj = EmployerProfile.objects.get(user_id=request.user)
            obj.company_name=fullname
            obj.industry=industry
            obj.location=location
            obj.description=description
            obj.save()
            return redirect('employer_profile')
    else:
        user = EmployerProfile.objects.get(user_id=request.user)
        form = EmployerUpdateProfileForm(instance=user)
    return render(request, 'employer_profile_update.html', {'form': form})

@login_required(login_url='employer_login')
def employer_profile(request):
    profile = EmployerProfile.objects.get(user_id=request.user)
    return render(request, 'employer_profile.html', {'profile': profile})

@login_required(login_url='employer_login')
def job_listing_page(request):
    employer = EmployerProfile.objects.get(user_id=request.user)
    job_listings = Job.objects.filter(employer=employer)
    
    context = {
        'job_listings': job_listings
    }
    return render(request, 'employer_job_listings.html', context)

@login_required(login_url='head_login')
def students_list(request):
    students = StudentProfile.objects.all()
    return render(request, 'head_student_list.html', {'students': students})
