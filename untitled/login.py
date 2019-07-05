from django.http import HttpResponse
from sqlite3 import *
# 读url传递过来的参数
def home(request):
    token = request.GET.get('token')
    username = request.GET.get('username')
    email = request.GET.get("email")
    phone = request.GET.get('phone')
    if token == 'SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW':
        return HttpResponse('Your token is : ' + token + " powered by Python + Django")
    else:
        return HttpResponse('CHECK YOUR TOKEN')