from ast import Mod
from email.policy import default
from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=355)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Employer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    National_id = models.IntegerField()
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,default="male")
    job_title = models.CharField(max_length=255)

class watermeter(models.Model):
    address = models.CharField(max_length=255)
    ownername = models.CharField(max_length=255)

class Customer(models.Model):
    watermeterid = models.ForeignKey(watermeter,default = 1,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    names = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,default="male")
    National_id = models.IntegerField()
    phonenumber = models.CharField(max_length=255, default="947587986")

class Bill(models.Model):
     w_id = models.ForeignKey(watermeter, on_delete = models.CASCADE)
     data_paid = models.DateField()
     bill_no_paid = models.CharField(max_length=255)
     bills_owner = models.CharField(max_length=255)
