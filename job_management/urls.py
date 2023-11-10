# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('student/employers/', views.student_employer_list, name='student_employer_list'),
    path('head/employers/', views.head_employer_list, name='head_employer_list'),
    path('student/jobs/', views.student_job_list, name='student_job_list'),
    path('head/jobs/', views.head_job_list, name='head_job_list'),
    path('head/student/verify/<int:student_id>/', views.head_student_verify, name='head_student_verify'),
    path('head/student/unverify/<int:student_id>/', views.head_student_unverify, name='head_student_unverify'),
    path('head/student/delete/<int:student_id>/', views.head_student_delete, name='head_student_delete'),
    path('head/employer/verify/<int:employer_id>/', views.head_employer_verify, name='head_employer_verify'),
    path('head/employer/unverify/<int:employer_id>/', views.head_employer_unverify, name='head_employer_unverify'),
    path('head/employer/delete/<int:employer_id>/', views.head_employer_delete, name='head_employer_delete'),
    path('jobs/create/', views.create_job, name='create_job'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit_job'),
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete_job'),
    path('jobs/apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('jobs/applications/', views.student_application_list, name='student_application_list'),
    path('application/shortlist/<int:application_id>/', views.shortlist_student, name='shortlist_student'),
    path('application/generate_shortlisted_students_pdf/<int:job_id>', views.generate_shortlisted_students_pdf, name='generate_shortlisted_students_pdf'),
]
