from django.db import models

# Create your models here.

class Provider(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    lang=models.CharField(max_length=122)
    curr=models.CharField(max_length=122)

    def __str__(self):
        return self.name

class Services(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    price=models.CharField(max_length=122)

    def __str__(self):
        return {self.city}