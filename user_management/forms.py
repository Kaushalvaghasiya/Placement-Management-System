# forms.py

from django import forms
from .models import CustomUser

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