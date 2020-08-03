from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    userId = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "orders")
    productType = models.IntegerField()
    selectedTheme = models.IntegerField()
    tires = models.IntegerField()
    currency = models.CharField(max_length = 20, blank = True)
    price = models.IntegerField()
    status = models.IntegerField()
    createdTime = models.DateTimeField()
    completedTime = models.DateTimeField()
        
    def __str__(self):
        return "order" + str(self.id)

    class Meta:
        ordering =("-pk",)