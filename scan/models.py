from django.db import models
from order.models import Order
# Create your models here.

class Scan(models.Model):
    scanId = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "scans")
    title = models.CharField(max_length= 300, blank = True);
    scanImageRaw = models.CharField(max_length = 300, blank = True)
    scanImageUrl = models.CharField(max_length = 300, blank = True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering =("-pk",)
    
    