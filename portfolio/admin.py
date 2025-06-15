from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'logo', 'is_active')
    search_fields = ('name', 'website')
    list_filter = ('is_active',)
