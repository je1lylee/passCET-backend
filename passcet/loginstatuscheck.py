from django.http import HttpResponse
import time
from passcet import models
def loginstatuscheck(request):
    token = request.POST.get('token')
    id = request.POST.get('id')
    ctime = request.POST.get('time') #(UNIX时间戳)从安卓本地的存储中返回上一次验证登录的时间如果没有的话就重新登录吧。。
    cimei = request.POST.get('imei')
    if token =='SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW' and id != None and cimei != None:
        if time.time()-ctime >= 15*24*60:
            return HttpResponse('超时')
        usermodel = models.passcet_user.objects.filter(id=id)
        return HttpResponse('ok')
    elif token !='SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW':
        return HttpResponse('{"code":"201","status":"Token错误"}')
    elif id == None or cimei == None:
        return HttpResponse('{"code":"202","status":"缺少参数"}')