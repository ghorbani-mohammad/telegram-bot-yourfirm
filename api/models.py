from django.db import models


class Profile(models.Model):
    user_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.user_id}"


class Subscription(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    term = models.CharField(max_length=255, blank=True, null=True)
    last_sent_job = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.term}"

    class Meta:
        unique_together = ["profile", "term"]


class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
