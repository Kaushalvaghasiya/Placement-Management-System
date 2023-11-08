# user_management/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Common fields for all user types
    email = models.EmailField(unique=True)
    user_type = models.CharField(choices=[('student', 'Student'), ('head', 'Head'), ('employer', "Employer")], max_length=10)
    full_name = models.CharField(max_length=100)
    # Other common fields
    def __str__(self):
        return self.user
    
class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
     # Semester SPI fields
    spi_semester1 = models.FloatField(null=True)
    spi_semester2 = models.FloatField(null=True)
    spi_semester3 = models.FloatField(null=True)
    spi_semester4 = models.FloatField(null=True)
    spi_semester5 = models.FloatField(null=True)
    spi_semester6 = models.FloatField(null=True)
    spi_semester7 = models.FloatField(null=True)
    spi_semester8 = models.FloatField(null=True)

    # CGPA field
    cgpa = models.FloatField(null=True, editable=False)
    resume = models.FileField(upload_to='resumes/')
    is_verified = models.BooleanField(default=False)

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
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
