from django.contrib import admin
from .models import BloodBank,Order

# Register your models here.

class BloodBankAdmin(admin.ModelAdmin):
    list_display = ('blood_bank_name','o_pos_group','o_neg_group','a_pos_group','a_neg_group','b_pos_group','b_neg_group','ab_pos_group','ab_neg_group')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','orderDetails','totalQuantity','is_delivered','created_at','updated_at')
    list_editable = ('is_delivered',)
    ordering = ('-id',)

admin.site.register(BloodBank,BloodBankAdmin)
admin.site.register(Order, OrderAdmin)