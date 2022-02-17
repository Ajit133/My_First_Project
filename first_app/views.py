from curses.ascii import HT
from re import template
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from first_app.models import Musician,Album

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    dic1 = {"text_1":"i am Programmar","musician":musician_list}
    return render(request,'first_app/index.html',context=dic1)