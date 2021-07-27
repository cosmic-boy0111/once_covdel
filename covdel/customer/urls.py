from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name="custHome"),
    path('aboutcustomer', views.aboutcustomer, name="custabout"),
    path('tracker', views.tracker, name="custTrackingStatus"),
    path('productView', views.productView , name="custProductview"),
    path('checkout', views.checkout , name="custCheckout"),
]