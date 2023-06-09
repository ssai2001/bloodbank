from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='hospital_home'),
    path('menu/<int:bb_id>',views.menu,name='hospital_menu'),
    path('cart/',views.cart,name='hospital_cart'),
    path('add-to-cart/',views.addToCart,name='add_to_cart'),
    path('delete/<str:b_group>',views.delete,name='delete_from_cart'),
    path('place-order/',views.placeOrder,name='place_order'),
    path('track-order/',views.trackOrder,name='hospital_track_order'),
    path('order-history/',views.orderHistory,name='hospital_order_history'),
    # Track Order
    path('ajax-view/',views.my_ajax_view,name='ajax_view')
]
