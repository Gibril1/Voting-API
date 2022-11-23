from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Nomination(models.Model):
    PORTFOLIO_CHOICES = (
        ('P', 'President'),
        ('M', 'Minister'),
        ('MP', 'Parliamentarian'),
        ('H', 'Head Of State'),
        ('D', 'DCE')
    )
    nominee = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    portfolio = models.CharField(max_length=3, choices=PORTFOLIO_CHOICES)
    description = models.TextField()
    acceptance = models.BooleanField(default=False)

    def __str__(self):
        return self.nominee


class Voting(models.Model):
    contestant = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.contestant} - {self.votes}'