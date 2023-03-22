from django.contrib import admin
from .models import BloodAvailability

# Register your models here.

class BloodAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('b_group','quantity')

admin.site.register(BloodAvailability, BloodAvailabilityAdmin)