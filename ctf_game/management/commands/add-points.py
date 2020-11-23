from django.core.management.base import BaseCommand
from ctf_game.models import Flag, Team

class Command(BaseCommand):
    help = 'Adds points to all teams according to the currently captured flags. \
            This command should be fired periodically (with cron for example).'

    def handle(self, *args, **options):
        # teams = Team.objects.all()
        flags = Flag.objects.all()
        teams = []
        for flag in flags:
            team = flag.owner
            team.score += flag.worth
            teams.append(team)
        Team.objects.bulk_update(teams, ['score'])

        self.stdout.write(self.style.SUCCESS('Successfully added points to teams.'))