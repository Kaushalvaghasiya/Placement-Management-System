# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('employers/', views.employer_list, name='employer_list'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/create/', views.create_job, name='create_job'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit_job'),
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete_job'),
    path('jobs/apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('review_applications/', views.employer_review_applications, name='employer_review_applications'),
    path('shortlist/<int:application_id>/', views.shortlist_candidate, name='shortlist_candidate'),
    path('send_invitation/<int:application_id>/', views.send_interview_invitation, name='send_interview_invitation'),
]
