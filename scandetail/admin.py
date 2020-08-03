from django.contrib import admin
from .models import ScanDetail
# Register your models here.

class ScanDetailAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScanDetail, ScanDetailAdmin)
