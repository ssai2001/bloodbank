from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='hospital_home'),
    path('cart/',views.cart,name='hospital_cart'),
    path('add-to-cart/',views.addToCart,name='add_to_cart'),
    path('track-order/',views.trackOrder,name='hospital_track_order'),
    path('order-history/',views.orderHistory,name='hospital_order_history')
]
