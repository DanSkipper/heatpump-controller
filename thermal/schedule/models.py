from django.db import models


class Action(models.Model):
    power = models.BooleanField(default=False)
    temperature = models.IntegerField(default=17)
    mode = models.IntegerField(default=0)
    fan = models.IntegerField(default=0)

    active = models.BooleanField(default=True)

    # time eg 1546 = 46mins after 3pm
    time = models.IntegerField(default=0)
    repeating = models.BooleanField(default=False)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)
    sunday = models.BooleanField(default=True)


class Settings(models.Model):
    # set this to false to turn off all alarms
    active = models.BooleanField(default=True)

    # True=24hr time, False=12hr time
    use24hr = models.BooleanField(default=True)