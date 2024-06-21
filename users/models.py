from django.db import models
from django.contrib.auth.models import User
from .constants import GENDER_TYPE

# Create your models here.

class UserLibraryAccount(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    memberId = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    birth_date = models.DateField(null=True,blank=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2,null=True,blank=True)
    def __str__(self):
        return str(self.memberId)
    

class UserAddress(models.Model):
    user = models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.email)
    