from django.db import models

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length= 10)
    passw = models.CharField(max_length=20,blank= False)
    email = models.CharField(max_length= 20)
    def __str__(self):
        return self.user