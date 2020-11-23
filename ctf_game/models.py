from django.db import models
from django.db.models import Sum

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    score = models.FloatField(default=0)

    def add_points(self):
        """Add points points according to the captured flag.
        Should be called periodically (with a cronjob for example).
        """
        captured_flags = Flag.objects.filter(owner_id=self.id)
        earned_points = captured_flags.aggregate(Sum('worth'))['worth__sum']
        if earned_points:
            self.score += earned_points

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name} ({self.score})"

class Flag(models.Model):
    name = models.CharField(max_length=50)
    worth = models.FloatField()
    owner = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        if self.owner:
            return f"{self.name} ({self.worth}) | {self.owner}"
        else:
            return f"{self.name} ({self.worth})"