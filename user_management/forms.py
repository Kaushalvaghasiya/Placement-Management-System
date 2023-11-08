# forms.py

from django import forms
from django.views.generic import UpdateView
from .models import CustomUser, StudentProfile, EmployerProfile

class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('full_name','username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'student'
        if commit:
            user.save()
        return user

class HeadSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('full_name','username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'head'
        if commit:
            user.save()
        return user

class EmployerSignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('full_name','username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'employer'
        if commit:
            user.save()
        return user
    
class StudentUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude = ['user','is_verified']
    widgets = {
        'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
    }

class EmployerUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        exclude = ['user','is_verified']