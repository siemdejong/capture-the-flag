from django.db import models
from django.db.models import Sum

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    score = models.FloatField(default=0)

    def add_points():
        """Add points points according to the captured flag.
        Should be called periodically (with a cronjob for example).
        """
        flags = Flag.objects.all()
        teams = []
        for flag in flags:
            team = flag.owner
            team.score += flag.worth
            teams.append(team)
        Team.objects.bulk_update(teams, ['score'])

    def reset_points():
        """Reset points of all teams."""
        teams = Team.objects.all()
        for team in teams:
            team.score = 0
        Team.objects.bulk_update(teams, ['score'])

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