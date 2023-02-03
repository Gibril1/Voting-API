from django.db import models
from django.contrib.auth.models import User
from elections.models import Election




class Portfolio(models.Model):
    portfolio = models.CharField(max_length=30,  null=True, default='')
    description = models.TextField(default='')
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.portfolio




    

class Voting(models.Model):
    contestant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='contestant')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name='voter')
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return self.voter