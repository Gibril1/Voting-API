from django.contrib import admin
from .models import Nomination, Voting


# Register your models here.
admin.site.register(Nomination)
admin.site.register(Voting)
