from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def home_page(request):
    #return HttpResponse(template.render(context))
    return render(request, 'home.html')
