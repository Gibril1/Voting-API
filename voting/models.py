from django.db import models
from django.contrib.auth.models import User
from elections.models import Election









    

class Voting(models.Model):
    contestant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='contestant')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name='voter')
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return self.voter