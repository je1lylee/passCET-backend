# 获取用户生词表
from passcet import settingfile as SF
from django.http import HttpResponse
from passcet import models
import json
def getwordlist(request):
    token = request.POST.get('token')
    userid = request.POST.get('userid')
    if token != SF.PASSCET_TOKEN or token == None:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    elif userid == None:
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        print('执行逻辑')
        QuerySett = models.passcet_glossary.objects.filter(user_id=userid) #QuerySet
        return HttpResponse(json.dumps(list(QuerySett.values())))