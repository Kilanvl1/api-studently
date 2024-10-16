from django.contrib import admin
from django.utils.html import format_html

from .models import Profile


@admin.register(Profile)
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone_number",
        "profile_status",
        "clickable_session_replay_url",
    ]
    search_fields = ["name", "phone_number"]
    list_filter = ["has_booked_appointment"]

    def clickable_session_replay_url(self, obj):
        if obj.session_replay_url:
            return format_html(
                '<a href="{}" target="_blank">Click here</a>',
                obj.session_replay_url,
            )
        return "No session replay found"

    clickable_session_replay_url.short_description = "Session Replay URL"

    def profile_status(self, obj):
        if obj.has_booked_appointment:
            return format_html("<span style='color: green;'>Meeting booked</span>")
        elif obj.is_lead:
            return format_html("<span style='color: orange;'>Lead</span>")
        elif not obj.is_eligible:
            return format_html("<span style='color: purple;'>Semi-Lead</span>")
        else:
            return format_html("<span style='color: red;'>No-lead</span>")
