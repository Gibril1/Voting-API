from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Election(models.Model):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)
    startAt = models.DateTimeField()
    duration = models.DurationField()



class Portfolio(models.Model):
    PORTFOLIO_CHOICES = (
        ('P', 'President'),
        ('M', 'Minister'),
        ('MP', 'Parliamentarian'),
        ('H', 'Head Of State'),
        ('D', 'DCE')
    )

    portfolio = models.CharField(max_length=3, choices=PORTFOLIO_CHOICES)

    def __str__(self):
        return self.portfolio


class Nomination(models.Model):
    campaign_name = models.CharField(unique=True, null=False, max_length=20, default='')
    description = models.TextField()
    acceptance = models.BooleanField(default=False)
    nominee = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.campaign_name

class Candidate(models.Model):
    nomination = models.OneToOneField(Nomination, on_delete=models.CASCADE)
    

class Voting(models.Model):
    contestant = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='contestant')
    voter = models.OneToOneField(User, on_delete=models.CASCADE, null = True, related_name='voter')

    def __str__(self):
        return f'{self.contestant} - {self.votes}'