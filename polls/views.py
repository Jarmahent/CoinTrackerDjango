from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import os
import random
#from . import pynance





def getPrice(request):
    if request.method == 'GET':
        #info = pynance.Pynance(pynance.key, pynance.secret)
        #price = info.get_usd_coin(86, "price")
        price = random.randint(1, 255)
        return HttpResponse(price)
    else:
        return HttpResponse("Bad post method!")




def index(request):

    template = loader.get_template("polls/index.html")
    return HttpResponse(template.render())
    #return HttpResponse("Hello Index.html", "/polls/index.html")



def indextwo(request):

    return render(request, "polls/index.html")
