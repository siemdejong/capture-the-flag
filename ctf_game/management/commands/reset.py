from django.core.management.base import BaseCommand
from ctf_game.models import Flag, Team

class Command(BaseCommand):
    help = 'Rest the points of all teams.'

    def handle(self, *args, **options):
        Team.reset_points()
        self.stdout.write(self.style.SUCCESS('Successfully added points to teams.'))