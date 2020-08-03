from django.db import models
from order.models import Order

# Create your models here.
class Payment(models.Model):
    orderId = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = "payments")
    cardName = models.CharField(max_length = 300, blank = True)
    cardNumber = models.IntegerField(blank = True)
    cvv = models.IntegerField(blank = True)
    price = models.IntegerField(blank = True)
    transactionCode = models.CharField(max_length = 300, blank = True)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        ordering =("-pk",)