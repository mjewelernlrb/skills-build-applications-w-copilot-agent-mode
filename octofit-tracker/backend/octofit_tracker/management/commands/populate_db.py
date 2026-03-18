from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()


        # Create Users (team is a string field)
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Team Marvel')
        captain = User.objects.create(email='cap@marvel.com', name='Captain America', team='Team Marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='Team DC')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='Team DC')

        # Create Teams with members
        marvel = Team.objects.create(name='Team Marvel', members=[ironman.email, captain.email])
        dc = Team.objects.create(name='Team DC', members=[batman.email, superman.email])

        # Create Activities (user is a string field: email)
        Activity.objects.create(user=ironman.email, type='run', duration=30, date='2023-01-01')
        Activity.objects.create(user=captain.email, type='cycle', duration=60, date='2023-01-02')
        Activity.objects.create(user=batman.email, type='swim', duration=45, date='2023-01-03')
        Activity.objects.create(user=superman.email, type='run', duration=50, date='2023-01-04')

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning cardio session', difficulty='Easy')
        Workout.objects.create(name='Strength Training', description='Full body strength workout', difficulty='Hard')

        # Create Leaderboard (team is a string field)
        Leaderboard.objects.create(team=marvel.name, points=190)
        Leaderboard.objects.create(team=dc.name, points=205)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))