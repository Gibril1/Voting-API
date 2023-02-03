from django.db import models
from django.contrib.auth.models import User
from elections.models import Election
# Create your models here.
class Nomination(models.Model):
    nominee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now=True)
    updatedAt = models.DateField(auto_now_add=True)
    acceptance = models.BooleanField(default=False)
    
    def __str__(self):
        return self.acceptance
