from django.http import HttpResponse
import time
from passcet import models
from passcet import settingfile as SF
# author : NsuMicClub:Liguodong
def loginstatuscheck(request):
    token = request.POST.get('token')
    id = request.POST.get('id')
    # ctime = request.POST.get('time') #(UNIX时间戳)从安卓本地的存储中返回上一次验证登录的时间如果没有的话就重新登录吧。。
    cimei = request.POST.get('imei')
    if token == SF.PASSCET_TOKEN and id != None and cimei != None:
            userInfo = models.passcet_user.objects.filter(id=id)
            return checkInfo(userInfo,cimei)
    elif token != SF.PASSCET_TOKEN:
        return HttpResponse(SF.PASSCET_201_TOKEN_ERROR)
    elif id == None or cimei == None:
        return HttpResponse(SF.PASSCET_202_PARAMETER_ERROR)
def checkInfo(userInfo,cimei):
    if str(userInfo[0].lastimei) == cimei and time.time() - userInfo[0].logintime > 15*24*60:
        return HttpResponse(SF.PASSCET_107_USERINFO_CHECK_SUCCESS)
    else:
        return HttpResponse(SF.PASSCET_203_NEED_LOGIN)