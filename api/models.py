from django.db import models


class Profile(models.Model):
    user_id = models.CharField(max_length=20, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Subscription(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term = models.CharField(max_length=255, blank=True, null=True)
    last_sent_job = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["profile", "term"]


class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
