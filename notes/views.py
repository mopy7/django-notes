from django.shortcuts import render
from django.http import HttpResponse


def testing(request):
    return HttpResponse("Notes app is working")
