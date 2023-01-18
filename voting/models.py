from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Election(models.Model):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    createdAt = models.DateField(default=timezone.now)
    updatedAt = models.DateField(auto_now_add=True)
    startAt = models.DateTimeField(null=False)
    endAt = models.DateTimeField(null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



class Portfolio(models.Model):
    PORTFOLIO_CHOICES = (
        ('P', 'President'),
        ('M', 'Minister'),
        ('MP', 'Parliamentarian'),
        ('H', 'Head Of State'),
        ('D', 'DCE')
    )

    portfolio = models.CharField(max_length=3, choices=PORTFOLIO_CHOICES,  unique=True, null=True, default='')
    description = models.TextField(default='')
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.portfolio


class Nomination(models.Model):
    nominee = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)
    acceptance = models.BooleanField(default=False)
    
    def __str__(self):
        return self.acceptance

    

class Voting(models.Model):
    contestant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='contestant')
    voter = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name='voter')

    def __str__(self):
        return self.voter