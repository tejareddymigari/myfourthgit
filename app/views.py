from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
def teja(request):
    return HttpResponse('<h1><marquee>teja reddy</marquee> </h1>')
def nandu(request):
    return HttpResponse('<h2><marquee>nandu reddy</marquee> <h2>')