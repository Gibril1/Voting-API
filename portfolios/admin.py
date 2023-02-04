from django.contrib import admin
from .models import Portfolio

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'portfolio'
    )
admin.site.register(Portfolio, PortfolioAdmin)
