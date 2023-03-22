from django.db import models

# Create your models here.

class BloodAvailability(models.Model):
    b_group = models.CharField(max_length=5)
    quantity = models.IntegerField()

    def __str__(self):
        return self.b_group
    
