from django.test import TestCase
from .models import Team, Flag

# Create your tests here.
class TeamModelTest(TestCase):
    def test_add_points(self):
        # Setup the database.
        team_one = Team(name='team_one')
        team_one.save()
        Flag.objects.create(name='flag_one', worth=1, owner=team_one)

        # Add up all the points associated with the captured flags.
        team_one.add_points()
        self.assertEqual(team_one.score, 1)