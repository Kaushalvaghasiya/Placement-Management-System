# views.py

from django.shortcuts import render, redirect
from .models import Notification
from user_management.models import CustomUser

def send_notification_to_all_students(sender, notification_type, message):
    student_users = CustomUser.objects.filter(user_type="student")

    for student_user in student_users:
        recipient = student_user
        send_notification(sender, recipient, notification_type, message)

def send_notification_to_all_heads(sender, notification_type, message):
    head_users = CustomUser.objects.filter(user_type="head")

    for head_user in head_users:
        recipient = head_user
        send_notification(sender, recipient, notification_type, message)

def send_notification(sender, recipient, notification_type, message):
    notification = Notification(sender=sender, recipient=recipient, notification_type=notification_type, message=message)
    notification.save()

def list_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user, is_read=False).order_by('-created_at')
    return render(request, 'list_notifications.html', {'notifications': notifications})

def mark_as_read(request, notification_id):
    notification = Notification.objects.get(pk=notification_id)
    if notification.recipient == request.user:
        notification.is_read = True
        notification.save()
    return redirect("list_notifications")
