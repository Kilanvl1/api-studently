from django.contrib import admin
from django.utils.html import format_html

from .models import Profile


@admin.register(Profile)
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "has_booked_appointment",
        "number_of_landingpage_visits",
        "clickable_session_replay_url",
    ]
    search_fields = ["name", "email"]
    list_filter = ["has_booked_appointment", "number_of_landingpage_visits"]

    def clickable_session_replay_url(self, obj):
        if obj.session_replay_url:
            return format_html(
                '<a href="{}" target="_blank">Click here</a>',
                obj.session_replay_url,
            )
        return "No session replay found"

    clickable_session_replay_url.short_description = "Session Replay URL"
