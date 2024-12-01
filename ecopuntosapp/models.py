from django.db import models

# Create your models here.

class Accounts(models.Model):
    username = models.CharField(max_length= 15)
    password = models.CharField(max_length= 15)
    trust = models.IntegerField()
    moderator = models.IntegerField(default= 0 )

def __str__(self):
    return self.name

class Objects(models.Model):
    name =  models.CharField(max_length=20)
    descripction = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    
def __str__(self):
    return self.name