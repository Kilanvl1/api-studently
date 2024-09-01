from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    session_replay_url = models.URLField(null=True)
    has_booked_appointment = models.BooleanField(default=False)
    number_of_landingpage_visits = models.IntegerField(default=1)
    age = models.IntegerField(null=True)
    is_student = models.BooleanField(null=True)
    is_dutch = models.BooleanField(null=True)
    is_EU = models.BooleanField(null=True)
    is_eligible = models.BooleanField(null=True)
    is_insured = models.BooleanField(null=True)
    has_insurance_benefit = models.BooleanField(null=True)
    is_working = models.BooleanField(null=True)
    is_living_at_home = models.BooleanField(null=True)

    @property
    def is_at_risk_of_insurance_fine(self):
        return self.is_working and not self.is_insured

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
