from django.urls import path
from . import views

urlpatterns = [
    path('donor/signin',views.donor_signin,name='donor_signin'),
    path('hospital/signin',views.hospital_signin,name='hospital_signin'),
    path('donor/signup',views.donor_signup,name='donor_signup'),
    path('hospital/signup',views.hospital_signup,name='hospital_signup'),
    path('logout',views.log_out,name='logout')
]
