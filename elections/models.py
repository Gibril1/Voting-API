from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Election(models.Model):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    createdAt = models.DateTimeField(default=timezone.now)
    updatedAt = models.DateTimeField(auto_now_add=True)
    startAt = models.DateTimeField(null=True)
    duration = models.DurationField(null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name