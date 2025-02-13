from django.contrib import admin
from import_export.admin import ExportMixin
from .models import SystemConfig, Revenue

class SystemConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key',)

class RevenueAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('date', 'amount')
    list_filter = ('date',)
    search_fields = ('date',)
    ordering = ('-date',)

admin.site.register(SystemConfig, SystemConfigAdmin)
admin.site.register(Revenue, RevenueAdmin)
