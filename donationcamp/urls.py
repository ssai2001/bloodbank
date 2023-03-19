from django.urls import path
from . import views

urlpatterns = [
    path('organize/',views.organize,name='organize'),
    path('verifyCamp/',views.verifyCamp,name='verifyCamp'),
    path('startCamp/',views.startCamp,name='startCamp'),
    path('donate/',views.donate,name='donate'),
    path('del/',views.delete_entry)
]
