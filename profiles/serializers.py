from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    number_of_landingpage_visits = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "name",
            "email",
            "has_booked_appointment",
            "number_of_landingpage_visits",
            "age",
            "is_student",
            "is_dutch",
            "is_EU",
            "is_eligible",
            "is_insured",
            "has_insurance_benefit",
            "is_working",
            "is_living_at_home",
        ]
        read_only_fields = ["id"]
        write_only_fields = ["email"]
