from django.http import HttpResponse
from passcet import settingfile as SF
from passcet.utils.takeLog import takelog
from passcet import models
import json


def getlearningtime(request):
    token = request.POST.get('token')
    userid = request.POST.get('userid')
    if token != None and token == SF.PASSCET_TOKEN:
        if userid != None:
            queryset = models.passcet_time.objects.filter(userid=userid)  # QuerySet
            takelog(__file__,json.dumps(list(queryset.values())))
            return HttpResponse(json.dumps(list(queryset.values())))
        else:
            takelog(__file__,SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)

    else:
        takelog(__file__,SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)