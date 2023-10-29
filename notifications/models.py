from django.db import models
from user_management.models import CustomUser

class Notification(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_notifications')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_notifications')
    notification_type = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification from {self.sender.username} to {self.recipient.username}"