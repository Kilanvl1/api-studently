from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    number_of_landingpage_visits = serializers.IntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "name",
            "email",
            "has_booked_appointment",
            "number_of_landingpage_visits",
        ]

    def create(self, validated_data):
        validated_data["email"] = validated_data["email"].lower()
        profile = Profile.objects.filter(email=validated_data["email"]).first()
        if profile:
            profile.number_of_landingpage_visits += 1
            profile.save()
        else:
            profile = Profile.objects.create(**validated_data)

        return profile
