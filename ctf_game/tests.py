from django.test import TestCase
from .models import Team, Flag
from io import StringIO
from django.core.management import call_command

# Create your tests here.
class TeamModelTest(TestCase):
    def test_add_points(self):
        # Setup the database.
        team_one = Team(name='team_one')
        team_two = Team(name='team_two')
        team_one.save()
        team_two.save()

        flag_one = Flag(name='flag_one', worth=1, owner=team_one)
        flag_two = Flag(name='flag_two', worth=2, owner=team_two)
        flag_one.save()
        flag_two.save()

        # Add up all the points associated with the captured flags.
        team_one.add_points()
        team_two.add_points()

        self.assertEqual(team_one.score, 1)
        self.assertEqual(team_two.score, 2)

    def test_add_points_command_output(self):
        out = StringIO()
        call_command('add-points', stdout=out)
        self.assertIn('Success', out.getvalue())
    