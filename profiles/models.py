from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    session_replay_url = models.URLField(null=True)
    has_booked_appointment = models.BooleanField(default=False)
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

    @property
    def is_lead(self):
        return self.is_EU and self.is_eligible and not self.has_booked_appointment

    @property
    def benefit_amount(self):
        if self.is_dutch:
            earnings = "1,455.96" if self.is_living_at_home else "3,628.68"
        else:
            earnings = "3,628.68" if self.has_insurance_benefit else "5,104.68"
        return earnings

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
