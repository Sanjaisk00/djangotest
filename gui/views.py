from django.shortcuts import render
import RPi.GPIO as GPIO


def dashboard(request):

    return render(request, 'index.html')
