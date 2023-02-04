from django.db import models
from django.contrib.auth.models import User
from elections.models import Election

# Create your models here.
class Portfolio(models.Model):
    portfolio = models.CharField(max_length=30,  null=True, default='')
    description = models.TextField(default='')
    election = models.ForeignKey(Election, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=200, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.portfolio
