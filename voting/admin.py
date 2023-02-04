from django.contrib import admin
from .models import (
    Voting, 
    
)

class VotingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'voter',
        'contestant'
    )


# Register your models here.
admin.site.register(Voting, VotingAdmin)



