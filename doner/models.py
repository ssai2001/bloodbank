from django.db import models
from user.models import customUser

# Create your models here.

class Coupons(models.Model):
    user = models.ForeignKey(customUser,on_delete=models.DO_NOTHING)
    couponCode = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
