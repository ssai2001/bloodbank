from django.contrib import admin
from .models import BloodDepot,Order

# Register your models here.

class BloodDepotAdmin(admin.ModelAdmin):
    list_display = ('b_group','quantity','price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','orderDetails','totalPrice','is_delivered','created_at','updated_at')
    list_editable = ('is_delivered',)
    ordering = ('-id',)

admin.site.register(BloodDepot, BloodDepotAdmin)
admin.site.register(Order, OrderAdmin)