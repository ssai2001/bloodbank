from django.db import models
from user.models import customUser

# Create your models here.

class BloodDepot(models.Model):
    b_group = models.CharField(max_length=5)
    quantity = models.IntegerField()
    price = models.FloatField()
    # image = models.ImageField(upload_to='')

    def __str__(self):
        return self.b_group

class Orders(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.DO_NOTHING)
    orderDetails = models.CharField(max_length=500)
    totalPrice = models.FloatField()
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
