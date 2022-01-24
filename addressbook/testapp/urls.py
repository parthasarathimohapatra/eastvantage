from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('createaddress',CreateAddress.as_view()),
    path('getaddress',AddressDetails.as_view()),
    path('editaddress',AddressEdit.as_view()),
    path('deleteaddress',DeleteAddress.as_view()),
]