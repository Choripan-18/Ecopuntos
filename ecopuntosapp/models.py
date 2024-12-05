from django.db import models

# Create your models here.

class useraccounts(models.Model):
    username = models.CharField(max_length= 15)
    password = models.CharField(max_length= 15)
    email = models.CharField(max_length= 25)
    trust = models.IntegerField(default=0)
    moderator = models.IntegerField(default= 0)

    

def __str__(self):
    return self.username

class Objects(models.Model):
    objname =  models.CharField(max_length=20)
    descripction = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    
def __str__(self):
    return self.objname

opciones_pedidas = [
    [0, "objeto"],
    [1, "lugar"]
]

class userrequest(models.Model):
    reqname = models.CharField(max_length=20)
    reqemail = models.CharField(max_length=30)
    typereq = models.IntegerField(choices=opciones_pedidas)
    requestext = models.TextField(max_length=200)
def __str__(self):
    return self.reqname

class Post(models.Model):
    author = models.CharField(max_length=100) 
    message = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.author