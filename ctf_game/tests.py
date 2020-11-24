from django.test import TestCase
from .models import Team, Flag
from io import StringIO
from django.core.management import call_command
from django.db.models import Sum

# Create your tests here.
class TeamModelTest(TestCase):
    def setUp(self):
        """Setup the database."""
        team_one = Team.objects.create(name='team_one')
        team_two = Team.objects.create(name='team_two')

        flag_one = Flag.objects.create(name='flag_one', worth=1, owner=team_one)
        flag_two = Flag.objects.create(name='flag_two', worth=2, owner=team_two)

    def test_add_points(self):
        """Test the add_points() attribute of the Teams model."""
        teams = Team.objects.all()
        flags = Flag.objects.all()

        Team.add_points()
        self.assertEqual(teams[0].score, 1)
        self.assertEqual(teams[1].score, 2)

    def test_add_points_command_output(self):
        """Test the add-points commandoutput."""
        out = StringIO()
        call_command('add-points', stdout=out)
        self.assertIn('Success', out.getvalue())
    
    def test_reset_points(self):
        """Test the reset_points() attribute of the Team model."""
        # Give every team free points.
        teams = Team.objects.all()
        teams.update(score=1)
        # Reset the points.
        Team.reset_points()
        total_points = teams.aggregate(Sum('score'))['score__sum']

        self.assertEqual(total_points, 0)

    def test_reset_points_command_output(self):
        """Test the output of the reset command."""
        out = StringIO()
        call_command('reset', stdout=out)
        self.assertIn('Success', out.getvalue())
    