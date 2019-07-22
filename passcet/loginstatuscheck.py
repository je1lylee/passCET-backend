from django.http import HttpResponse
import time
from passcet import models
# author : NsuMicClub:Liguodong
def loginstatuscheck(request):
    token = request.POST.get('token')
    id = request.POST.get('id')
    # ctime = request.POST.get('time') #(UNIX时间戳)从安卓本地的存储中返回上一次验证登录的时间如果没有的话就重新登录吧。。
    cimei = request.POST.get('imei')
    if token =='SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW' and id != None and cimei != None:
            userInfo = models.passcet_user.objects.filter(id=id)
            return checkInfo(userInfo,cimei)
    elif token !='SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW':
        return HttpResponse('{"code":"201","status":"Token错误"}')
    elif id == None or cimei == None:
        return HttpResponse('{"code":"202","status":"缺少参数"}')
def checkInfo(userInfo,cimei):
    if str(userInfo[0].lastimei) == cimei and time.time() - userInfo[0].logintime > 15*24*60:
        return HttpResponse('{"code":"101","status":"OK"}')
    else:
        return HttpResponse('{"code":"203","status":"需要重新登录"}')