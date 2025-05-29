from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'twitter_token', 'facebook_token']
    search_fields = ['user__username']
