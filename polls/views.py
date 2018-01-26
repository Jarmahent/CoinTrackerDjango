from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
import os
from . import pynance



def home():
    return(str("Test for Template replace"))


def index(request):
    template = loader.get_template("polls/index.html", {"home": home})
    return HttpResponse(template.render(), )
    #return HttpResponse("Hello Index.html", "/polls/index.html")




def get_value(request):
    info = pynance.Pynance(pynance.key, pynance.secret)
    price = info.get_usd_coin(86, "price")
    return HttpResponse(price)


def indextwo(request):

    return render(request, "polls/index.html", {'home': home})
