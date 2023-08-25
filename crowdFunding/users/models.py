from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):


    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=13,null=True)
    picture = models.ImageField(upload_to='media/',null=True)
    status = models.CharField(max_length=100,default='user')
    birthday=models.DateField(null=True)
    country = models.CharField(max_length=100,default='Egypt')
    facebook_profile = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.username

