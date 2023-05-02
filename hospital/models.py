from django.db import models
from user.models import customUser

# Create your models here.
    
class BloodBank(models.Model):
    blood_bank_name = models.CharField(max_length=100)
    o_pos_group = models.IntegerField()
    o_neg_group = models.IntegerField()
    a_pos_group = models.IntegerField()
    a_neg_group = models.IntegerField()
    b_pos_group = models.IntegerField()
    b_neg_group = models.IntegerField()
    ab_pos_group = models.IntegerField()
    ab_neg_group = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.blood_bank_name

class Order(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.DO_NOTHING)
    orderDetails = models.CharField(max_length=500)
    totalQuantity = models.IntegerField(null=True)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
