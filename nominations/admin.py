from django.contrib import admin
from .models import Nomination

# Register your models here.
class NominationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'portfolio',
        'nominee'
    )
admin.site.register(Nomination, NominationAdmin)
