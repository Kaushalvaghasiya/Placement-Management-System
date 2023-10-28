from django.db import models
from user_management.models import StudentProfile, EmployerProfile
from datetime import datetime

# Create your models here.
class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    application_deadline = models.DateField()

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, default=None)
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(default=datetime.now)
    is_shortlisted = models.BooleanField(default=False)
    interview_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Application for {self.job.title} by {self.student.username}"

class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    interview_date = models.DateTimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Interview for {self.application.student_name}"