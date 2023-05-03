from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('navigation/<int:track_id>',views.navigation,name='navigation'),
    path('ajax-insert/',views.my_ajax_insert)
]
