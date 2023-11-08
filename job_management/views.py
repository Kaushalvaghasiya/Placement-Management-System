# views.py

from django.shortcuts import render, redirect
from user_management.models import EmployerProfile, StudentProfile, CustomUser
from .models import Job, Application
from .forms import EmployerForm, JobForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from notifications.views import send_notification_to_all_students, send_notification

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

@login_required(login_url='employer_login')
def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    applications = Application.objects.filter(job=job)
    student_details = []
    for application in applications:
        applied_date = application.applied_date
        student = application.student
        student_details.append({
            'id': student.id,
            'full_name': student.full_name,
            'email': student.user.email,
            'contact_number': student.contact_number,
            'CGPA': student.cgpa,
            'resume': student.resume,
        })
    return render(request, 'job_detail.html', {'job': job, 'students': student_details})

@login_required(login_url='employer_login')
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            user = EmployerProfile.objects.get(user=request.user)
            if user.is_verified:
                job.employer = user
                job.save()
                sender = request.user
                notification_type = "New Job Listing"
                message = "A new job listing has been posted. Check it out!"
                send_notification_to_all_students(sender, notification_type, message)
            return redirect('job_listing_page')
    else:
        form = JobForm()
    return render(request, 'create_job.html', {'form': form})

@login_required(login_url='employer_login')
def edit_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        user = EmployerProfile.objects.get(user=request.user)
        if user.is_verified:
            form = JobForm(request.POST, instance=job)
            if form.is_valid():
                form.save()
        return redirect('job_listing_page')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit_job.html', {'form': form, 'job': job})

@login_required(login_url='employer_login')
def delete_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        user = EmployerProfile.objects.get(user=request.user)
        if user.is_verified:
            job.delete()
        return redirect('job_listing_page')
    return render(request, 'delete_job.html', {'job': job})

@login_required(login_url='student_login')
def apply_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        student = StudentProfile.objects.get(user_id=request.user)
        if student.is_verified:
            try:
                application = Application.objects.get(job=job)
            except:
                application = Application(job=job, student=student)
                application.save()
        return redirect('student_job_list')
    return render(request, 'apply_job.html')

@login_required(login_url='student_login')
def student_application_list(request):
    user = StudentProfile.objects.get(user_id=request.user)
    applications = Application.objects.filter(student=user)
    job_details = []
    for application in applications:
        job = Job.objects.get(id=application.job.id)
        job_details.append({
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'applied_date': application.applied_date,
            'is_shortlisted': application.is_shortlisted,
            'interview_date': application.interview_date,
        })
    return render(request, 'student_application_list.html', {'jobs': job_details})

@login_required(login_url="head_login")
def head_student_verify(request, student_id):
    obj = StudentProfile.objects.get(id=student_id)
    obj.is_verified=True
    obj.save()
    return redirect('head_students_list')

@login_required(login_url="head_login")
def head_student_unverify(request, student_id):
    obj = StudentProfile.objects.get(id=student_id)
    obj.is_verified=False
    obj.save()
    return redirect('head_students_list')

@login_required(login_url="head_login")
def head_student_delete(request, student_id):
    student = CustomUser.objects.get(user_id=student_id)
    student.delete()
    obj = StudentProfile.objects.get(id=student_id)
    obj.delete()
    return redirect('head_students_list')

@login_required(login_url="head_login")
def head_employer_verify(request, employer_id):
    obj = EmployerProfile.objects.get(id=employer_id)
    obj.is_verified=True
    obj.save()
    return redirect('head_employer_list')

@login_required(login_url="head_login")
def head_employer_unverify(request, employer_id):
    obj = EmployerProfile.objects.get(id=employer_id)
    obj.is_verified=False
    obj.save()
    return redirect('head_employer_list')

@login_required(login_url="head_login")
def head_employer_delete(request, employer_id):
    student = CustomUser.objects.get(user_id=employer_id)
    student.delete()
    obj = EmployerProfile.objects.get(id=employer_id)
    obj.delete()
    return redirect('head_employer_list')


@login_required(login_url='employer_login')
def shortlist_student(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.is_shortlisted = True
    application.save()
    return redirect('employer_review_applications')

@login_required(login_url='employer_login')
def reject_student(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.is_shortlisted = False
    application.save()
    return redirect('employer_review_applications')

@login_required(login_url='employer_login')
def send_interview_invitation(request, application_id):
    application = Application.objects.get(pk=application_id)
    application.interview_date = datetime.now()
    application.save()
    return redirect('employer_review_applications')
