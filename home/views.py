from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime


def home(request):
    return JsonResponse({'hello': 'home', 'date': datetime.date.today()})
