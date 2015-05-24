from django.db import models

# Create your models here.


class HeatPumpState(models.Model):
    power = models.BooleanField(default=False)
    temperature = models.IntegerField(default=17)
    mode = models.IntegerField(default=0)
    fan = models.IntegerField(default=0)
