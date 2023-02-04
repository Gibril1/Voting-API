from django.contrib import admin
from .models import Election

# Register your models here.
class ElectionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
admin.site.register(Election, ElectionAdmin)
