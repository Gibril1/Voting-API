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
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio = models.CharField(max_length=3, choices=PORTFOLIO_CHOICES)
    description = models.TextField()
    acceptance = models.BooleanField()

    def __str__(self):
        return self.student