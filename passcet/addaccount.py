from django.http import HttpResponse
from django.template import RequestContext
import random
#只有在验证码验证成功的时候才可以调用
def addaccount(request):
    token = request.POST.get('token')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    leavel = request.POST.get('leavel')
    #  id由随机数生成，8位数字 如果重复了可能会报错？
    if token == 'SMvwlN1kjrtKzIfxCLHlejDedpVSTRvW':
        userId = giveMeId() #生成ID 对于判空的操作交给前端完成
        if(phone != None):
            return viaPhone(userId,phone,leavel)
        else:
            return viaEmail(userId,phone,leavel)
    else:
        return HttpResponse('{"status":"token-error"}')
def giveMeId():
    #ID生成器
    return random.randint(10000000,99999999)
def viaPhone(id,phone,leavel):
    return HttpResponse('viaphone')
def viaEmail(id,email,leavel):
    return HttpResponse('viaEmail')
    print('b')