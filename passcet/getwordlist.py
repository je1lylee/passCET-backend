# 获取用户生词表
from passcet import settingfile as SF
from django.http import HttpResponse
from passcet import models
from passcet.utils.takeLog import takelog
import json
def getwordlist(request):
    token = request.POST.get('token')
    userid = request.POST.get('userid')
    if token != SF.PASSCET_TOKEN or token == None:
        takelog(__file__,SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    elif userid == None:
        takelog(__file__,SF.PASSCET_202_PARAMETER_ERROR)
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        print('执行逻辑')
        QuerySett = models.passcet_glossary.objects.filter(user_id=userid) #QuerySet
        takelog(__file__,SF.PASSCET_101_OK)
        return HttpResponse(json.dumps(list(QuerySett.values())))