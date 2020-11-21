from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    score = models.FloatField()

class Flag(models.Model):
    name = models.CharField(max_length=50)
    worth = models.FloatField()
    bonus_on_capture = models.FloatField()
    owner = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
