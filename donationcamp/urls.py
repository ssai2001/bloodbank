from django.urls import path
from . import views

urlpatterns = [
    path('organize/',views.organize,name='organize'),
    path('startCamp/',views.startCamp,name='startCamp'),
    path('del/',views.delete_entry)
]
