from django.contrib import admin

from .models import Profile


@admin.register(Profile)
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "has_booked_appointment",
        "number_of_landingpage_visits",
    ]
    search_fields = ["name", "email"]
    list_filter = ["has_booked_appointment", "number_of_landingpage_visits"]
