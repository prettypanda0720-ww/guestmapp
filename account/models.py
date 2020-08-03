from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "profile")
    fbid = models.CharField(max_length = 20, blank = True)
    googleid = models.CharField(max_length = 20, blank = True)
    name = models.CharField(max_length = 20, blank = True)
    isFirstUser = models.BooleanField()
    

    


