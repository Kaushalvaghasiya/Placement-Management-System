# forms.py

from django import forms
from .models import Job, Application
from user_management.models import EmployerProfile

class EmployerForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['employer']
    widgets = {
        'interview_date': forms.DateInput(attrs={'type': 'date'}),
        'applied_date': forms.DateInput(attrs={'type': 'date'}),
    }
