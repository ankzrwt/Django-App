from django.db import models

# Create your models here.
class Customer(models.Model):
    customerId=models.CharField(max_length=20)
    phone=models.IntegerField()
    name=models.CharField(max_length=30)

class Account(models.Model):
    accountId=models.CharField(max_length=13)
    customerId=models.CharField(max_length=13)
    balance=models.IntegerField()


