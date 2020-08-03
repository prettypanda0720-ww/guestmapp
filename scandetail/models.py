from django.db import models
from scan.models import Scan

# Create your models here.
class ScanDetail(models.Model):
    scanId = models.ForeignKey(Scan, on_delete = models.CASCADE, related_name = "scandetails")
    email = models.CharField(max_length = 300, blank = True)
    content = models.CharField(max_length = 300, blank = True)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        ordering =("-pk",)
