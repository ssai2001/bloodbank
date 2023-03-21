from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='doner_home'),
    path('coupons/',views.coupons,name='doner_coupons'),
    path('participation/<str:user_email>',views.participation,name='doner_participation'),
]
