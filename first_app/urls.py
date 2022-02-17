from django.urls import re_path as url
from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index,name = 'index'),

]



