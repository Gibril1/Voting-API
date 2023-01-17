from django.contrib import admin
from .models import (
    Nomination, 
    Voting, 
    Portfolio, 
    Election,
)


# Register your models here.
admin.site.register(Nomination)
admin.site.register(Voting)
admin.site.register(Portfolio)
admin.site.register(Election)

