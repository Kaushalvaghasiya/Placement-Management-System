from django.contrib import admin
from . models import EmployerProfile, StudentProfile, CustomUser, HeadProfile

# Register your models here.
admin.site.register(EmployerProfile)
admin.site.register(StudentProfile)
admin.site.register(CustomUser)
admin.site.register(HeadProfile)