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
    campaign_name = models.CharField(unique=True, null=False, max_length=20, default='')
    portfolio = models.CharField(max_length=3, choices=PORTFOLIO_CHOICES)
    description = models.TextField()
    acceptance = models.BooleanField(default=False)

    def __str__(self):
        return self.campaign_name


class Voting(models.Model):
    contestant = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='contestant')
    votes = models.IntegerField(default=0)
    voter = models.OneToOneField(User, on_delete=models.CASCADE, null = True, related_name='voter')

    def __str__(self):
        return f'{self.contestant} - {self.votes}'