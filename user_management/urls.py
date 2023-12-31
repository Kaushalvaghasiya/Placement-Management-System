# user_management/urls.py

from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.student_login, name='student_login'),
    path('logout/', views.user_logout, name='logout'),
    path('head/students/', views.students_list, name='head_students_list'),
    path('student/signup/', views.student_signup, name='student_signup'),
    path('head/signup/', views.head_signup, name='head_signup'),
    path('employer/signup/', views.employer_signup, name='employer_signup'),
    path('head/login/', views.head_login, name='head_login'),
    path('employer/login/', views.employer_login, name='employer_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('head/dashboard/', views.head_dashboard, name='head_dashboard'),
    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/profile/update/', views.student_update_profile, name='student_profile_update'),
    path('employer/profile/', views.employer_profile, name='employer_profile'),
    path('employer/profile/update/', views.employer_update_profile, name='employer_profile_update'),
    path('job-listings/', views.job_listing_page, name='job_listing_page'),
]
