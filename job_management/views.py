# views.py

from django.shortcuts import render, redirect
from user_management.models import EmployerProfile
from .models import Job, Application
from .forms import EmployerForm, JobForm, ApplicationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

def employer_list(request):
    employers = EmployerProfile.objects.all()
    return render(request, 'employer_list.html', {'employers': employers})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'job_detail.html', {'job': job})

@login_required(login_url='employer_login')
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'create_job.html', {'form': form})

@login_required(login_url='employer_login')
def edit_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form, 'job': job})

@login_required(login_url='employer_login')
def delete_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'delete_job.html', {'job': job})

@login_required(login_url='student_login')
def apply_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.student = request.user
            application.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()
    return render(request, 'apply_job.html', {'form': form, 'job': job})

def employer_review_applications(request):
    applications = Application.objects.filter(job__employer=request.user)
    return render(request, 'employer_review_applications.html', {'applications': applications})

def shortlist_candidate(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.is_shortlisted = True
    application.save()
    return redirect('employer_review_applications')

def send_interview_invitation(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.interview_date = datetime.now() # Set the interview date
    application.save()
    return redirect('employer_review_applications')
