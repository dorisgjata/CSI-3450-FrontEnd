from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template=loader.get_template('index.html')
    context=None
    return HttpResponse(template.render(context,request))
def details(request, languagecode): 
    return HttpResponse("You're looking at language codes: %s" % (languagecode))
 