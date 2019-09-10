from django.http import HttpResponse
from passcet import settingfile as SF
from passcet import takelog
from passcet import models
# 记录用户的学习时间 需要创建time表，对应用户的userid，学习时长和记录的日期。
def pushlearningtime(request):
    token = request.POST.get('token')
    userid = request.POST.get('userid')
    learningtime = request.POST.get('leaningtime')
    datetime = request.POST.get('datetime')
    if token != None and token == SF.PASSCET_TOKEN:
        if userid != None and learningtime != None and datetime != None:
            try:
                models.passcet_time.objects.create(userid=userid,learningtime=learningtime,datetime=datetime)
                take_log(SF.PASSCET_101_OK)
                return HttpResponse(SF.PASSCET_101_OK)
            except:
                take_log(SF.PASSCET_213_DB_ERROR)
                return HttpResponse(SF.PASSCET_213_DB_ERROR)
        else:
            take_log(SF.PASSCET_202_PARAMETER_ERROR)
            return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
    else:
        take_log(SF.PASSCET_201_TOKEN_ERROR)
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)


def take_log(status):
    takelog.takelog('pushlearningtime',status)