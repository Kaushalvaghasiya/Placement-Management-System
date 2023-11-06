# views.py

from django.shortcuts import render, redirect
from user_management.models import EmployerProfile
from .models import Job, Application
from .forms import EmployerForm, JobForm, ApplicationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from notifications.views import send_notification_to_all_students

@login_required(login_url='student_login')
def student_employer_list(request):
    employers = EmployerProfile.objects.all()
    return render(request, 'student_employer_list.html', {'employers': employers})

@login_required(login_url='head_login')
def head_employer_list(request):
    employers = EmployerProfile.objects.all()
    return render(request, 'head_employer_list.html', {'employers': employers})


@login_required(login_url='student_login')
def student_job_list(request):
    jobs = Job.objects.all()
    return render(request, 'student_job_list.html', {'jobs': jobs})

@login_required(login_url='head_login')
def head_job_list(request):
    jobs = Job.objects.all()
    return render(request, 'head_job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'job_detail.html', {'job': job})

@login_required(login_url='employer_login')
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.employer_id=request.user
            form.save()
            sender = request.user
            notification_type = "New Job Listing"
            message = "A new job listing has been posted. Check it out!"
            send_notification_to_all_students(sender, notification_type, message)
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
        form = ApplicationForm(request.POST)
        if form.is_valid():
            print("HI")
            application = form.save(commit=False)
            application.job = job
            application.student = request.user
            application.save()
            return redirect('job_list')
    else:
        form = ApplicationForm()
    return render(request, 'apply_job.html', {'form': form, 'job': job})

@login_required(login_url='employer_login')
def employer_review_applications(request):
    applications = Application.objects.filter(job__employer=request.user)
    return render(request, 'employer_review_applications.html', {'applications': applications})

@login_required(login_url='employer_login')
def shortlist_candidate(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.is_shortlisted = True
    application.save()
    return redirect('employer_review_applications')

@login_required(login_url='employer_login')
def send_interview_invitation(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.interview_date = datetime.now() # Set the interview date
    application.save()
    return redirect('employer_review_applications')
