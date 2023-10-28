from django.contrib import admin
from .models import Job, Interview, Application

# Register your models here.
admin.site.register(Job)
admin.site.register(Interview)
admin.site.register(Application)