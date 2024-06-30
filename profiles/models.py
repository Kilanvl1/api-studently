from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    has_booked_appointment = models.BooleanField(default=False)
    number_of_landingpage_visits = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
