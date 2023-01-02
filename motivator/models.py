from django.db import models
from loginsystem.models import User
from loginsystem.views import login
class Activates(models.Model):
    pass
    # user = models.ForeignKey()
    # day_logins = models.DateTimeField(auto_now_add=True)
    # time_spend_in = models.DateTimeField(auto_now_add=True)


class Workouts(models.Model):
    pass


class BookReading(models.Model):
    pass

class PlayGames(models.Model):
    pass

class spending_family(models.Model):
    pass