from django.shortcuts import render, HttpResponse

# Create your views here.
def phonecases(request):
    return HttpResponse('Hello World! This is phonecases page.')
