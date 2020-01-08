from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):

    return render(request,'pages/index.html')

def about(request):
    #cart =  json.loads(request.session.get('cart'))
    #print(cart)

    return render(request,'pages/about.html')
