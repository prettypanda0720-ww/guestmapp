from django.contrib import admin
from .models import Scan
# Register your models here.

class ScanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Scan, ScanAdmin)

