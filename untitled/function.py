from django.http import *
import json
from django.http import HttpResponse

def home(request):
    return HttpResponse('running')