from django.urls import path
from .views import *
urlpatterns = [
    path('',dashboard,name='dashboard'),
    path('profile/',profile,name='profile'),
    path('sign_in/',sign_in,name='sign_in'),
    path('sign_up/',sign_up,name='sign_up'),
    path('forget_pass/',forget_pass,name='forget_pass'),
    path('otp_veify/',otp_veify,name='otp_veify'),
    
    path('settings/',settings,name='settings'),
    path('eror/',eror,name='eror'),
]