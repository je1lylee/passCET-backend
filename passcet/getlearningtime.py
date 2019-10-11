from django.http import HttpResponse
from passcet import settingfile as SF
from passcet import takelog
from passcet import models
import json


def getlearningtime(request):
    token = request.POST.get('token')
    userid = request.POST.get('userid')
    if token != None and token == SF.PASSCET_TOKEN:
        if userid != None:
            queryset = models.passcet_time.objects.filter(userid=userid)  # QuerySet
            take_log(json.dumps(list(queryset.values())))
            return HttpResponse(json.dumps(list(queryset.values())))
        else:
            take_log(SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)

    else:
        take_log(SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)


def take_log(status):
    takelog.takelog('getlearningtime', status)
