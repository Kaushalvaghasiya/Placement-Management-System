# user_management/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    # Common fields for all user types
    email = models.EmailField(unique=True)
    user_type = models.CharField(choices=[('student', 'Student'), ('head', 'Head'), ('employer', "Employer")], max_length=10)
    full_name = models.CharField(max_length=100)
    # Other common fields
    
class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    # Add academic fields (e.g., GPA, major, university, etc.)
    # Add resume field for file upload
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.user

class HeadProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    def __str__(self):
        return self.user

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.company_name
