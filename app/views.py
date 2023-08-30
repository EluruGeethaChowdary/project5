from django.shortcuts import render

from django.Http import  HttpResponse

def string_response(request):
 return HttpResponse('<marquee><h1>'this is chinni'</marquee></h1>')