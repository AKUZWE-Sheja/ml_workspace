from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def greetings(request):
    return HttpResponse("Hello World")

def render_my_page(request):
    template = loader.get_template("index.html")
    return HttpResponse()


