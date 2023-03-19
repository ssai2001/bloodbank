from django.db import models

# Create your models here.

class organizerDetails(models.Model):
    organizationName = models.CharField(max_length=100)
    organizerName = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    description = models.TextField()
    password = models.IntegerField()

class donerDetails(models.Model):
    organizerId = models.ForeignKey(organizerDetails,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.EmailField(default="null")
    b_group = models.CharField(max_length=5)
    contact = models.CharField(max_length=10)
