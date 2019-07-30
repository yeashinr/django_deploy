from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.testhome, name='thome'),
    path('tryform/',views.tryout, name='tryform'),  
]
