from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(request):
    date= datetime.datetime.now()
    msg = "<h1> Hello friend good Evening...!!!</h1>"
    msg += "<h1>Now Server time is " + str(date)+  "</h1>"
    return HttpResponse(msg)