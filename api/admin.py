from django.contrib import admin

from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "user_id", "created_at")


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("pk", "profile", "term", "created_at")


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("pk", "profile", "text", "sent_at")
