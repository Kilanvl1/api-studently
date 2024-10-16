from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    is_at_risk_of_insurance_fine = serializers.SerializerMethodField()
    benefit_amount = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "name",
            "email",
            "phone_number",
            "session_replay_url",
            "has_booked_appointment",
            "age",
            "is_student",
            "is_dutch",
            "is_EU",
            "is_eligible",
            "is_insured",
            "has_insurance_benefit",
            "is_working",
            "is_living_at_home",
            "is_at_risk_of_insurance_fine",
            "benefit_amount",
        ]

    @extend_schema_field(serializers.BooleanField())
    def get_is_at_risk_of_insurance_fine(self, obj):
        return obj.is_at_risk_of_insurance_fine

    @extend_schema_field(serializers.CharField())
    def get_benefit_amount(self, obj):
        return obj.benefit_amount

    """ def validate_phone_number(self, value):
        # Phone number should start with a + followed by country code digits, then a space, and then the phone number
        if not value.startswith("+"):
            raise serializers.ValidationError("Phone number should start with a +")

        parts = value[1:].split(" ", 1)
        if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
            raise serializers.ValidationError(
                "Phone number should be in the format: +country code phone number"
            )

        return value """
