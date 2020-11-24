from django.core.management.base import BaseCommand
from ctf_game.models import Team

class Command(BaseCommand):
    help = 'Adds points to all teams according to the currently captured flags. \
            This command should be fired periodically (with cron for example).'

    def handle(self, *args, **options):
        Team.add_points()
        self.stdout.write(self.style.SUCCESS('Successfully added points to teams.'))